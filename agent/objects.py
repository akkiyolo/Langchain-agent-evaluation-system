from pydantic import BaseModel,Field

class Answer(BaseModel):
  answer:str=Field(description="The answer that is needed for the user question")
  conversation:bool=Field(description="This is an indicator if conversation should still continue or not, if agent has made the decision about refund this should be False " \
  "If the conversation needs more talk this should be True", default=True)

class PurchaseItem(BaseModel):
  name:str=Field(description="Name of the item purchased")
  