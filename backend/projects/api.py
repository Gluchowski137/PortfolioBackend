from ninja import Router

router = Router()


@router.post("upload/")
def upload_image(_):
    return {"Succes": True}
