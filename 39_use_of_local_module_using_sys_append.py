import sys
sys.path.append("H:\\my_python_module")
import my_email as e 
e.SendTextEmail('anuradha@gmail.com','Test Subject','Test Email')
e.SendEmailWithAttachment('anuradha@gmail.com','Test Subject','Test Email','files')
