from .ui import UserAddWindow
from objectpack.actions import ObjectPack
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
import objectpack


class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    edit_window = add_window = objectpack.ui.ModelEditWindow.fabricate(model)


class UserPack(ObjectPack):
    model = User
    add_to_desktop = True
    edit_window = add_window = UserAddWindow


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_desktop = True
    edit_window = add_window = objectpack.ui.ModelEditWindow.fabricate(model)


class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = True

    def __init__(self, content_type_pack=None):
        self.edit_window = self.add_window = objectpack.ui.ModelEditWindow.fabricate(self.model, model_register={
            'ContentType': content_type_pack or ContentTypePack()
        })
        super().__init__()

