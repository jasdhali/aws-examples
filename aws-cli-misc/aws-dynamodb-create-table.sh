aws dynamodb create-table --table-name Music --attribute-definitions AttributeName=Artist,AttributeType=S AttributeName=SongTitle,AttributeType=S \
       --key-schema AttributeName=Artist,KeyType=HASH AttributeName=	
