# Kafka
we use kafka to create some event on some works that we don't need the answer on that time.
we use kafka to haven't latency in doing some big works.
we can use kafka in recognizing location of people.
we can use kafka in showing notifications.

### in this repository
in this repository i used kafka to create some file with a request, this is a simple app to show that how we can use kafka with python and how we can have a good structure for kafka in python

# running project
# First
go to env file and change the `SERVER_URL` to your ip address.

# Second
install The docker on your system


# Third
open a command on the project's path

# Forth
write on command `docker-compose up` and press `Enter`

# Fifth
go to a browser and search for this address `http://<your ip address>:5003/<name of your file>`

after you requested to application, the consumer will create a file in `/consumer/app/` with name was written by you in the url
