from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import src.controllers.skill as controllers
from src.dependencies.database import get_db
from src.dependencies.skill import get_skill_activity_or_404, get_skill_or_404
from src.dependencies.user import get_user_or_404
from src.models.skill import Skill
from src.models.skill_activity import SkillActivity
from src.models.user import User
from src.schemas.api_response import SuccessResponse
from src.schemas.skill import (
    SkillActivitiesCreateRequest,
    SkillActivitiesPartialUpdateRequest,
    SkillActivitiesResponse,
    SkillActivitiesUpdateRequest,
    SkillActivityResponse,
    SkillCreateRequest,
    SkillPartialUpdateRequest,
    SkillResponse,
    SkillsResponse,
    SkillUpdateRequest,
)

router = APIRouter(prefix="/skills", tags=["skills"])


@router.get("", status_code=HTTPStatus.OK, response_model=SuccessResponse[SkillsResponse])
def get_skills(
	user: User = Depends(get_user_or_404),
	db: Session = Depends(get_db)
) -> SuccessResponse[SkillsResponse]:
	return controllers.get_skills(
		user,
		db
	)


@router.post("", status_code=HTTPStatus.CREATED, response_model=SuccessResponse[SkillResponse])
def create_skill(
	payload: SkillCreateRequest,
	user: User = Depends(get_user_or_404),
	db: Session = Depends(get_db),
) -> SuccessResponse[SkillResponse]:
	return controllers.create_skill(
		payload,
		user,
		db
	)


@router.get("/{skill_id}", status_code=HTTPStatus.OK, response_model=SuccessResponse[SkillResponse])
def get_skill_by_id(
	skill: Skill = Depends(get_skill_or_404),
	db: Session = Depends(get_db)
) -> SuccessResponse[SkillResponse]:
	return controllers.get_skill_by_id(
		skill,
		db
	)

@router.put("/{skill_id}", status_code=HTTPStatus.OK, response_model=SuccessResponse[SkillResponse])
def update_skill_by_id(
	payload: SkillUpdateRequest,
	skill: Skill = Depends(get_skill_or_404),
	db: Session = Depends(get_db)
) -> SuccessResponse[SkillResponse]:
	return controllers.update_skill_by_id(
		payload,
		skill,
		db
	)


@router.patch("/{skill_id}", status_code=HTTPStatus.OK, response_model=SuccessResponse[SkillResponse])
def partial_update_skill_by_id(
	payload: SkillPartialUpdateRequest,
	skill: Skill = Depends(get_skill_or_404),
	db: Session = Depends(get_db)
) -> SuccessResponse[SkillResponse]:
	return controllers.partial_update_skill_by_id(
		payload,
		skill,
		db
	)



@router.post("/{skill_id}/activities", status_code=HTTPStatus.CREATED, response_model=SuccessResponse[SkillActivitiesResponse])
def create_skill_activities(
	payload: SkillActivitiesCreateRequest,
	skill: Skill = Depends(get_skill_or_404),
	db: Session = Depends(get_db)
) -> SuccessResponse[SkillActivitiesResponse]:
	return controllers.create_skill_activities(
		payload,
		skill,
		db
	)


@router.put("/{skill_id}/activities", status_code=HTTPStatus.OK, response_model=SuccessResponse[SkillActivitiesResponse])
def update_skill_activities(
	payload: SkillActivitiesUpdateRequest,
	skill: Skill = Depends(get_skill_or_404),
	db: Session = Depends(get_db)
) -> SuccessResponse[SkillActivitiesResponse]:
	return controllers.update_skill_activities(
		payload,
		skill,
		db
	)


@router.patch("/{skill_id}/activities", status_code=HTTPStatus.OK, response_model=SuccessResponse[SkillActivitiesResponse])
def partial_update_skill_activities(
	payload: SkillActivitiesPartialUpdateRequest,
	skill: Skill = Depends(get_skill_or_404),
	db: Session = Depends(get_db)
) -> SuccessResponse[SkillActivitiesResponse]:
	return controllers.partial_update_skill_activities(
		payload,
		skill,
		db
	)



@router.get("/{skill_id}/activities/{activity_id}", status_code=HTTPStatus.OK, response_model=SuccessResponse[SkillActivityResponse])
def get_skill_activity_by_id(
	activity: SkillActivity = Depends(get_skill_activity_or_404),
) -> SuccessResponse[SkillActivityResponse]:
	return controllers.get_skill_activity_by_id(
		activity,
	)


@router.delete("/{skill_id}/activities/{activity_id}", status_code=HTTPStatus.NO_CONTENT, response_model=None)
def delete_skill_activity_by_id(
	activity: SkillActivity = Depends(get_skill_activity_or_404),
	db: Session = Depends(get_db)
) -> None:
	return controllers.delete_skill_activity_by_id(
		activity,
		db
	)
