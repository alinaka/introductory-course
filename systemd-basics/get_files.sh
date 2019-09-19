#!/bin/bash
wget \
	--no-clobber \
	--page-requisites \
	--mirror \
	--html-extension \
	--convert-links \
	--domains $1 \
	--no-parent \
		$1	
