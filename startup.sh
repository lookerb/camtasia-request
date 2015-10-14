#!/bin/sh
# Starts pyramid application
# Created by David Hietpas (hietpasd@uwosh.edu)

nohup ./env/bin/pserve production.ini --pid-file=lock.pid --log-file=event.log >> event.log &
