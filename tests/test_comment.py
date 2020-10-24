import unittest
from app.models import Pitch,User,Comment
from app import db


class CommentModelTest(unittest.TestCase):
  def setUp(self):
    self.user_Hassan = User(username = 'Hassan',password = '123456', email = 'a@gmail.com')
    self.new_pitch = Pitch(pitch_title='Supermarket bs plan',pitch_body='This is a pitch about my new supermarket',pitch_category="Investors",user = self.user_Hassan )
    self.new_comment = Comment(comment='Test Comment',user=self.user_Hassan,pitch=self.new_pitch)

  def tearDown(self):
    Comment.query.delete()  
    Pitch.query.delete()
    User.query.delete()


  def test_check_instance_variables(self):
    '''
    Test if the values of variables are correctly being placed.
    '''
    self.assertEquals(self.new_comment.comment,'Test Comment')
    self.assertEquals(self.new_comment.user,self.user_Hassan)
    self.assertEquals(self.new_comment.pitch,self.new_pitch)


  def test_save_comment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comment.query.all())>0)
                 


 