import unittest
from app.models import Pitch,User
from app import db


class PitchModelTest(unittest.TestCase):
  def setUp(self):
    self.user_Hassan = User(username = 'Hassan',password = '123456', email = 'a@gmail.com')
    self.new_pitch = Pitch(pitch_title='Supermarket bs plan',pitch_body='This is a pitch about my new supermarket',pitch_category="Investors",user = self.user_Hassan )


  def tearDown(self):
    Pitch.query.delete()
    User.query.delete()  


  def test_check_instance_variables(self):
    '''
    Test if the values of variables are correctly being placed.
    '''
    self.assertEquals(self.new_pitch.pitch_title,'Supermarket bs plan')
    self.assertEquals(self.new_pitch.pitch_body,'This is a pitch about my new supermarket')
    self.assertEquals(self.new_pitch.pitch_category,'Investors')
    self.assertEquals(self.new_pitch.user,self.user_Hassan)              


  def test_save_pitch(self):
    '''
    Test for our save pitch method. We also query the database to confirm that we actually have data saved.
    ''' 
    self.new_pitch.save_pitch()
    self.assertTrue(len(Pitch.query.all())>0)


  def test_get_all_pitches(self):
    '''
    Test to see if we can get all saved pitches
    ''' 
    self.new_pitch.save_pitch()
    got_pitches = Pitch.get_all_pitches()
    self.assertTrue(len(got_pitches) == 1)  

  def test_get_user_pitches(self):

        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_user_pitches(self.new_pitch.user_id)
        self.assertTrue(len(got_pitches) == 1)       