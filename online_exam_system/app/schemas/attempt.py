from pydantic import BaseModel


class StartAttempt(BaseModel):
    student_id: int
    exam_id: int


class AnswerItem(BaseModel):
    question_id: int
    answer: str


class SubmitAttempt(BaseModel):
    attempt_id: int
    answers: list[AnswerItem]