
import unittest
from app.models import Pitch,User
from app import db

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        self.user_nazarine = User(username = 'nazarine',password = 'naz48810', email = 'nazarinewasonga48@gmail.com')
        self.new_comment = Comment(pitch_id=1234,pitch_title='create comment',comment_pitch='web developers are the best',user = self.user_nazarine)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch,'An opening forum for youths')
        self.assertEquals(self.new_pitch.user,self.user_nazarine)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        get_pitches = Pitch.get_all_piches()
        self.assertTrue(len(got_pitches) == 1)