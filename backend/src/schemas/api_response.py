from typing import Union, Dict, Any
from fastapi.responses import JSONResponse


def SuccessResponse(
	status_code: int,
	message: str = "Request Successful",
	data: Union[Dict[str, Any], None] = None
) -> JSONResponse:
	return JSONResponse(
		status_code=status_code,
		content={
			"message": message,
			"data": data
		}
	)
