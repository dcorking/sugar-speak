#!/bin/bash
# This script bsed on a template from the Fedora Project wiki
# https://fedoraproject.org/wiki/Packaging/SugarActivityGuidelines#Sample_Checkout_Script
# 
# sugar-speak-checkout.sh
VERSION=9
NAME=Speak
rm -rf $NAME-$VERSION
git clone git://dev.laptop.org/activities/speak $NAME-$VERSION
tar -cjvf $NAME-$VERSION.tar.bz2 $NAME-$VERSION
rm -rf $NAME-$VERSION
