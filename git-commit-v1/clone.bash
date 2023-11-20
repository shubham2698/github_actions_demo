#!/bin/bash

if [ "${{ inputs.repository }}" != "." ]; then
    git clone https://${{ inputs.token }}@github.com/${{ inputs.repository }}.git
    cd ${{ inputs.repository-name }}
    git checkout ${{ inputs.branch }}
          
fi