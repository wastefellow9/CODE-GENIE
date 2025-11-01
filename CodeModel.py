from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import time

def generate_code(prompt):
    model_id = "Salesforce/codegen-350M-multi"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)

    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

    start = time.time()
    sequences = pipe(prompt, max_length=128, do_sample=True, temperature=0.7)
    end = time.time()

    output = sequences[0]['generated_text']
    return output, start, end
