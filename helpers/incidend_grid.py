class IncidentGrid:
    def __init__(self):
        self.grid = []
        self.incidents_count = len(self.grid)

    def add_incident(self, incident):
        self.grid.append(incident)

    def remove_incident(self, incident_number):
        for incident in self.grid:
            if incident.number == incident_number:
                self.grid.remove(incident)


class Incident:
    def __init__(self, number, problem, priority, state, assignment, opened=None, desc="", caller="", tags=None,
                 created="", updated="", updated_by=""):
        self.number = number
        self.problem = problem
        self.opened = opened
        self.desc = desc
        self.caller = caller
        self.tags = tags
        self.priority = priority
        self.state = state
        self.assignment = assignment
        self.created = created
        self.updated = updated
        self.updated_by = updated_by

    def is_applicable(self):
        return True if self.state == "Active" or self.state == "New" else False

    def open_incident(self):
        self.number.click()
