#!/bin/bash
export P4A_RELEASE_KEYSTORE=~/keystores/RMCYTA.keystore
export P4A_RELEASE_KEYSTORE_PASSWD=L3tmein11
export P4A_RELEASE_KEYALIAS_PASSWD=L3tmein11
export P4A_RELEASE_KEYALIAS=RMCYTA
buildozer android release 
