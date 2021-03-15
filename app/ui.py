from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__lastlogin = ext.ExtDateField(
            label=u'last login',
            name='last login',
            format='d.m.Y',
            anchor='100%')

        self.field__superuserstatus = ext.ExtCheckBox(
            label=u'superuser status',
            name='superuser status',
            anchor='100%')

        self.field__firstname = ext.ExtStringField(
            label=u'first name',
            name='first name',
            allow_blank=False,
            anchor='100%')

        self.field__lastname = ext.ExtStringField(
            label=u'last name',
            name='last name',
            allow_blank=False,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email address',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__staffstatus = ext.ExtCheckBox(
            label=u'staff status',
            name='staff status',
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label=u'active',
            name='active',
            anchor='100%')

        self.field__datejoined = ext.ExtDateField(
            label=u'date joined',
            name='date joined',
            format='d.m.Y',
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__lastlogin,
            self.field__superuserstatus,
            self.field__firstname,
            self.field__lastname,
            self.field__email,
            self.field__staffstatus,
            self.field__active,
            self.field__datejoined,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'
