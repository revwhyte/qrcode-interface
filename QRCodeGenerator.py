import qrcode
# https://pypi.org/project/qrcode/
# img = qrcode.make(text)
# img.save(filename)

"""
Standard and common parameters for creating an object
    - base_url
    - name
    - email
    - address
    - telephone
    - github_username
"""

class QRCodeGenerator():
    def __init__(self, **kwargs) -> None:
        self.img = None
        for val in kwargs.keys():
            setattr(self, val, kwargs[val])

    ''' OBJECT PROPERTIES '''
    @property
    def generic(self) -> str:
        ''' TODO: Creates an URL with GET parameters using each attribute from the object '''
        return ""

    @property
    def github_profile(self) -> str:
        ''' returns a string as a GitHub profile URL '''
        return str(f"{self.url}/{self.profile}")

    ''' OBJECT METHODS '''
    def __str__(self) -> str:
        ''' returns the object as readable text '''
        output: str = ""
        
        for attr in self.__dict__:
            output += f"{str(attr)} => '{getattr(self, attr)}'\n"
        
        return output

    def generate(self, prop) -> None:
        ''' receives a virtual property as argument, generates QRCode and saves it inside the object's image '''
        self.img = qrcode.make(prop)

    def save(self) -> None:
        ''' exports the image with a default name (same directory as code) '''
        self.img.save('qrcode.png')

# Testing
qr: QRCodeGenerator = QRCodeGenerator(plain_text="123 som teste")
qr.generate(qr.plain_text)
qr.save()