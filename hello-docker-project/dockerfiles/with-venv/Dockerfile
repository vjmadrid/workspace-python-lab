FROM python:3.9-alpine


# ***************************
# *** Prepare Environment ***
# ***************************

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m venv $VIRTUAL_ENV


# ********************
# *** Prepare Code ***
# ********************

# Option 2
WORKDIR /app

COPY * .



# ****************************
# *** Prepare Dependencies ***
# ****************************
#RUN pip install --upgrade pip
RUN pip install -r requirements.txt



# ***************
# *** Execute ***
# ***************

CMD ["python", "main.py"]
# CMD [ "./bin/make-main"] 