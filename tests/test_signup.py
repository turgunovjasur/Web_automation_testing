from .test_base import BaseTest
from actions.login_action import LoginActions


class TestSignUp(BaseTest):

    def test_signup(self):
        self.signup = LoginActions(self.driver)
        assert self.signup.login_actions("xamidjonov2016@gamil.com", "mynameispasswordXXZ12*")