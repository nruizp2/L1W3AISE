import google.generativeai as genai
import os

def generate_response(prompt, chain:False):
    """
    Generate a response based on the given prompt using the GEMINI model.

    Args:
        prompt (str): The prompt to generate a response for.

    Returns:
        None
    """
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Generate a response using the GEMINI model
    if not chain:
        response = model.generate_content(prompt)
        # Print the prompt and the generated response
        print(f"Prompt:\n{prompt}\n")
        print(f"Response:\n{response.text}")
    else:
        for i in prompt:
            response = model.generate_content(i)
            print(f"Prompt:\n{i}\n")
            print(f"Response:\n{response.text}")

#Few Shot Prompt
print("Few Shot Prompt:\n")
promt = " ".join(open("Point 3\Few-Shot-Prompt.txt", "r").readlines())
generate_response(promt, False)

#CoT Prompt
print("CoT Prompt:\n")
prompt = " ".join(open("Point 3\CoT-Promt.txt", "r").readlines())
generate_response(prompt, False)

#Promt Chain:
print("Promt Chain:\n")
promts = open("Point 3\Promt-Chain.txt", "r").readlines()
generate_response(promts, chain=True)

#Tree of thoughts
print("Tree of thoughts:\n")
promt = " ".join(open("Point 3\Tree-of-thoughts.txt", "r").readlines())
generate_response(promt, False)


