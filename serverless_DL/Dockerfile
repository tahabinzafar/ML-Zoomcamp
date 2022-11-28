FROM svizor42/zoomcamp-dino-dragon-lambda:v2

RUN pip install pip install Pillow
RUN pip install requires.io
RUN pip install urllib3
RUN pip install numpy
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl


COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]