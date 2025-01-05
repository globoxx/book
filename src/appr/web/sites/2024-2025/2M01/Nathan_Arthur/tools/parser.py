import os

class Note:
    def __init__(self, branch, score, nameTest, subset=None):
        self.branch = branch
        self.score = score
        self.name = nameTest
        self.subset = subset

    def __repr__(self):
        return f"Note(branch={self.branch}, score={self.score}, subset={self.subset})"
class Results:
    def __init__(self, filePath, version):
        self.version = version
        self.notes = []
        self.info = []
    
    def parse_lines(self, lines):
        for line in lines:
            if line.startswith("version:"):
                self.info.append(("version", line.split(":")[1].strip()))
            elif line.startswith("name:"):
                self.info.append(("name", line.split(":")[1].strip()))
            elif line.startswith("surname:"):
                self.info.append(("surname", line.split(":")[1].strip()))
            elif line.startswith("mail:"):
                self.info.append(("mail", line.split(":")[1].strip()))
            elif line.startswith("username:"):
                self.info.append(("username", line.split(":")[1].strip()))
            else:
                elements = line.strip().split(',')
                if len(elements) >= 3:
                    branch = elements[0].strip()
                    score = elements[1].strip()
                    nameTest = elements[2].strip()
                    subset = elements[3] if len(elements) > 3 else None
                    self.notes.append(Note(branch, float(score), nameTest, subset))

    
    def reconstruct_lines(self):
        lines = []
        for key, value in self.info:
            lines.append(f"{key}: {value}")
        for note in self.notes:
            lines.append(f"{note.branch}, {note.score}, {note.name}, {note.subset}")
        return lines
            
    def get_info(self, key):
        for item in self.info:
            if item[0] == key:
                return item[1]
        return None       

    def add_note(self, branch, score, name, subset=None):
        try:
            new_note = Note(branch, float(score), name, subset)
            self.notes.append(new_note)
            return True
        except ValueError as ve:
            return(f"Invalid score value: {ve}")
            
        except Exception as e:
            return(f"Error adding note: {e}")
            
        
    def remove_note(self, branch, score, name):
        try:
            for note in self.notes:
                if note.branch == branch and note.score == float(score) and note.name == name:
                    self.notes.remove(note)
                    return True
            return("Note not found")
            
        except ValueError as ve:
            return(f"Invalid score value: {ve}")
            
        except Exception as e:
            return(f"Error removing note: {e}")
    
    def update_note(self, branch, name_old, name, score, subset=""):
        for note in self.notes:
            if note.branch == branch and note.name == name_old:
                note.name = name
                note.score = score
                note.subset = subset
                break


    @property    
    def calcul_average(self):
        branch_scores = {}
        for note in self.notes:
            if isinstance(note.branch, list):
                branch = note.branch[0]
            else:
                branch = note.branch
            if branch not in branch_scores:
                branch_scores[branch] = []
            branch_scores[branch].append(note.score)

        result = {}
        for branch in branch_scores:
            average = sum(branch_scores[branch])/len(branch_scores[branch])
            rounded_average = round(average * 2) / 2
            result[branch] = rounded_average
        
        return result
        