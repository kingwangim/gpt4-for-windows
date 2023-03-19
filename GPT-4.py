# install 
# pip install steamship

from steamship import Steamship

# Create a Steamship client
# NOTE: When developing a package, just use `self.client`
client = Steamship(workspace="gpt-4")

# Create an instance of this generator
generator = client.use_plugin('gpt-4')

# Get the questions
question = input("Input what you want to ask to GPT-4: \n")

# Generate text
task = generator.generate(text=question)

# Wait for completion of the task.
task.wait()

# Print the output
print(task.output.blocks[0].text)
