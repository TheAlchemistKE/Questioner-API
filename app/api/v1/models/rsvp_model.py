from .base_model import BaseModel
class RsvpModel(BaseModel):
    def create_rsvp(self, data):
        return BaseModel.save_data(self, db="rsvp", data=data)
        
    
        