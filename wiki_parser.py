import wikipediaapi

"""

This program allows the user to query information from the Wikipedia API based on:
    - The page title (as shown on Wikipedia)
    - Objectives (keywords to filter by)
    
Filtering through the returned page sections will yield a list of complete and partial matches to each objective.
This can be implemented in the future to gather current or additional information by the model.
This is an important feature because it will allow the model to widen its own resources.

One possible fallacy of this idea could be fact-checking one websites data based on data gathered from another 
website. This opens the door for incorrect information to be labeled as correct information, which would effect the 
model going forward.

This functionality can be expanded upon, for example, using web-scraping to gather information from websites that do 
not implement their own API.

"""

# Setup API
WIKI_user_agent = "wikipedia-api/1.0"
WIKI_headers = {'User-Agent': WIKI_user_agent}

WIKI = wikipediaapi.Wikipedia('en', headers=WIKI_headers)

# Setup query
query_page = "Harry Potter"
query_objectives = ["Voldemort", "Harry Potter"]

# Request API
res_page = WIKI.page(query_page)
res_sections = res_page.sections

# Parse
query_objective_contexts = {objective: {"complete": [], "partial": []} for objective in query_objectives}

# If a section has subsections, its main section component will be empty. Need to empty subsections
real_sections = []
for section in res_sections:
    if not section.text:
        for sub_section in section.sections:
            real_sections.append(sub_section)
        else:
            real_sections.append(section)

# Match objectives to pertinent text sections from query response
for section in real_sections:
    for objective in query_objectives:  # Iterate through each objective
        if section.text.find(objective) != -1:  # found complete objective in text
            query_objective_contexts[objective]["complete"].append(section)
        else:
            for partial_objective in objective.split(' '):
                if section.text.find(partial_objective) != -1:  # found partial objective in text
                    query_objective_contexts[objective]["partial"].append(section)
