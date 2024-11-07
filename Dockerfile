FROM python

RUN pip install pyqrcode
RUN pip install pypng

COPY pyqrcode_main.py /opt
ENV PYQRCODE_ERROR=H
ENV PYQRCODE_VERSION=
ENV PYQRCODE_MODE=
ENV PYQRCODE_FGCOLOR=red
ENV PYQRCODE_BGCOLOR=white

WORKDIR /app

ENTRYPOINT [ "python", "/opt/pyqrcode_main.py" ]
