from django.conf.urls import url
from objectpack import desktop
from .controller import controller
from .actions import ContentTypePack
from .actions import GroupPack
from .actions import PermissionPack
from .actions import UserPack

def register_urlpatterns():
	"""
	Регистрация конфигурации урлов для приложения
	"""
	return [url(*controller.urlpattern)]


def register_actions():
	"""
	Регистрация экшен-паков
	"""
	content_type_pack = ContentTypePack()
	permission_pack = PermissionPack(content_type_pack=content_type_pack)
	return controller.packs.extend([
		content_type_pack,
		GroupPack(),
		permission_pack,
		UserPack(),
	])

def register_desktop_menu():
	"""
	регистрация элементов рабочего стола
	"""
	desktop.uificate_the_controller(
    	    controller,
    	    menu_root=desktop.MainMenu.SubMenu('Demo'),
	)
