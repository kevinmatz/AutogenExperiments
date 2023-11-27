import os
import openai
# import mammoth
# import textwrap
# import pandoc
import argparse

parser = argparse.ArgumentParser(description="Program to proofread a Microsoft Word file using an OpenAI LLM",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("src", help="Source file, a Microsoft Word document")
parser.add_argument("dest", help="Destination file, a Microsoft Word document")

args = parser.parse_args()
config = vars(args)
# print("Config:")
# print(config)

sourceFilename = config["src"]
destinationFilename = config["dest"]

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

print("sourceFilename: " + sourceFilename)
print("destinationFilename: " + destinationFilename)
print("OPENAI_API_KEY: " + openai.api_key)

"""
# Convert Word to Markdown
with open("input.docx", "rb") as docx_file:
    result = mammoth.convert_to_markdown(docx_file)
    md_text = result.value

# Break the markdown text into segments
segments = textwrap.wrap(md_text, 2048)

# Proofread each segment
proofread_segments = []
prompt_format = "please perform copy editing on this text to correct spelling, grammar, usage, and punctuation mistakes: {}"

for segment in segments:
    prompt = prompt_format.format(segment)
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=2100
    )
    # Save the corrected text
    proofread_segments.append(response.choices[0].text.strip())

# Reassemble the proofread markdown
proofread_md = ' '.join(proofread_segments)

# Write the proofread markdown to a file
with open('proofread.md', 'w') as file:
    file.write(proofread_md)

# using pandoc to convert the markdown back to word document.
os.system("pandoc -s proofread.md -o proofread.docx")

print("Proofreading is complete. The proofread document is 'proofread.docx'")
"""
