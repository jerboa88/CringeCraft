import requests
import json

jenkinsApiUrl = 'https://ci.ender.zone/job/EssentialsX/lastSuccessfulBuild/api/json?tree=artifacts[relativePath]'
artifactsToMatch = ['EssentialsX-', 'EssentialsXDiscord-', 'EssentialsXDiscordLink-']

response = requests.get(jenkinsApiUrl)
responseData = json.loads(response.text)

for artifact in responseData['artifacts']:
	relativePath = artifact['relativePath']
	fileName = relativePath.split('/')[-1]

	for artifactToMatch in artifactsToMatch:
		if artifactToMatch in relativePath:
			fileData = requests.get("https://ci.ender.zone/job/EssentialsX/lastSuccessfulBuild/artifact/" + relativePath)

			try:
				with open(fileName, 'wb') as file:
					file.write(fileData.content)
			except Exception as e:
				print("Error writing the file content: ", e)
