import io
import pyautogui


class Image:

    @classmethod
    def get_screenshot(cls):
        return pyautogui.screenshot()

    @classmethod
    def get_screenshot_as_byte_array(cls):
        img = pyautogui.screenshot()
        return cls._image_to_byte_array(img)

    @classmethod
    def _image_to_byte_array(cls, img):
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        return img_byte_arr.getvalue()
