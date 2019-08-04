from django.test import TestCase
from .models import *


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user='James', image='james.png')
        self.profile.save()

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))


class Projects_TestCases(TestCase):
    def setup(self):
        self.user_me = User(id=1, username='Bright', email='be.rightmuk@gmail.com', password='qwerty123')
        self.user_me.save()
        self.me_profile = Profile(user=self.user_me, bio='best programmer', profile_pic='/media/profile.png', contact='0723219840')
        self.me_profile.save()
        self.my_project = Project(id=1, user= self.user_me, profile= self.me_profile, sitename='pigdice', screenshot='/media/pig.png', link='http://pigdice.herokuapp.com',technologies='javascript')
        self.my_project.save()
        self.the_review = Review(id=1,project=self.my_project,user=self.user_me, text='i like it')
        self.the_review.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Project.objects.all().delete()
        Review.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user_me,User))
        self.assertTrue(isinstance(self.me_profile,Profile))
        self.assertTrue(isinstance(self.my_project,Project))
        self.assertTrue(isinstance(self.the_review,Review))

    def test_delete_method(self):
        self.my_project.save_project()
        object = Project.objects.filter(id=1)
        Project.delete_project(object)
        all_objects = Project.objects.all()
        self.assertTrue(len(all_objects) == 0)


    def test_get_project_by_id(self):
        self.my_project.save_project()
        project = Project.get_project_by_id(1)
        self.assertEqual(project.id,1)


    def test_update_project(self):
        self.my_project.save_project()
        filtered_object =Project.update_project('muk','Greener')
        updated = Project.objects.get(name='Greener')
        self.assertEqual(updated.name,'Greener')

    def test_search_by_name(self,search_term):
        self.project.save_project()
        got_project = Project.objects.get(sitename=search_term)
        self.assertTrue(got_project.sitename=='pigdice')