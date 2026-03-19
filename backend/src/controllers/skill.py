from sqlalchemy.orm import Session

import src.services.skill as services
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


def get_skills(
	user: User,
	db: Session
) -> SuccessResponse[SkillsResponse]:

	return SuccessResponse[SkillsResponse](
		message="Skills fetched successfully",
		data=services.get_skills(
			user,
			db
		)
	)


def create_skill(
	payload: SkillCreateRequest,
	user: User,
	db: Session
) -> SuccessResponse[SkillResponse]:

	return SuccessResponse[SkillResponse](
		message="Skill created successfully",
		data=services.create_skill(
			payload,
			user,
			db
		)
	)


def get_skill_by_id(
	skill: Skill,
	db: Session
) -> SuccessResponse[SkillResponse]:
	
	return SuccessResponse[SkillResponse](
		message="Skill fetched successfully",
		data=services.get_skill_by_id(
			skill,
			db
		)
	)


def update_skill_by_id(
	payload: SkillUpdateRequest,
	skill: Skill,
	db: Session
) -> SuccessResponse[SkillResponse]:
	
	return SuccessResponse[SkillResponse](
		message="Skill updated successfully",
		data=services.update_skill_by_id(
			payload,
			skill,
			db
		)
	)


def partial_update_skill_by_id(
	payload: SkillPartialUpdateRequest,
	skill: Skill,
	db: Session
) -> SuccessResponse[SkillResponse]:

	return SuccessResponse[SkillResponse](
		message="Skill updated successfully",
		data=services.partial_update_skill_by_id(
			payload,
			skill,
			db
		)
	)


def create_skill_activities(
	payload: SkillActivitiesCreateRequest,
	skill: Skill,
	db: Session
) -> SuccessResponse[SkillActivitiesResponse]:

	return SuccessResponse[SkillActivitiesResponse](
		message="Skill activities created successfully",
		data=services.create_skill_activities(
			payload,
			skill,
			db
		)
	)


def update_skill_activities(
	payload: SkillActivitiesUpdateRequest,
	skill: Skill,
	db: Session
) -> SuccessResponse[SkillActivitiesResponse]:

	return SuccessResponse[SkillActivitiesResponse](
		message="Skill activities updated successfully",
		data=services.update_skill_activities(
			payload,
			skill,
			db
		)
	)


def partial_update_skill_activities(
	payload: SkillActivitiesPartialUpdateRequest,
	skill: Skill,
	db: Session
) -> SuccessResponse[SkillActivitiesResponse]:

	return SuccessResponse[SkillActivitiesResponse](
		message="Skill activities updated successfully",
		data=services.partial_update_skill_activities(
			payload,
			skill,
			db
		)
	)


def get_skill_activity_by_id(
	activity: SkillActivity,
) -> SuccessResponse[SkillActivityResponse]:

	return SuccessResponse[SkillActivityResponse](
		message="Skill activity fetched successfully",
		data=services.get_skill_activity_by_id(
			activity,
		)
	)


def delete_skill_activity_by_id(
	activity: SkillActivity,
	db: Session
) -> None:
	
	services.delete_skill_activity_by_id(
		activity,
		db
	)
