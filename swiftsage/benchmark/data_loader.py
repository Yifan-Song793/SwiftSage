import json
import os
import re
import random
from typing import Any, Iterable, Union

from datasets import Dataset, concatenate_datasets, load_dataset

from swiftsage.benchmark.data_utils import (
    lower_keys,
    parse_question,
    parse_ground_truth,
)


def load_jsonl(file):
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                yield json.loads(line)
            except:
                print("Error in loading:", line)
                exit()


def load_data(
        data_name,
    ):
    if data_name == "gpqa":
        dataset = load_dataset("Idavidrein/gpqa", "gpqa_diamond", split="train")
        tmp_examples = list(dataset)
        examples = []
        random.seed(42)
        for idx, example in enumerate(tmp_examples):
            list_choices = [example['Incorrect Answer 1'], example['Incorrect Answer 2'], example['Incorrect Answer 3'], example['Correct Answer']]
            random.shuffle(list_choices)
            abcd = "ABCD"
            answer = abcd[list_choices.index(example['Correct Answer'])]
            
            options = list_choices
            assert len(options) == 4
            for i, (label, option) in enumerate(zip('ABCD', options)):
                options[i] = f"({label}) {str(option).strip()}"
            options = ", ".join(options)

            examples.append({
                "id": idx,
                "question": f"{example['Question'].strip()}\nWhat of the following is the right choice? Explain your answer.\n{options}",
                "answer": answer,
            })
        dataset = examples
    elif data_name == "math-l5":
        dataset = load_dataset("AI-MO/aimo-validation-math-level-5", split="train")
        dataset = dataset.rename_column("problem", "question")
    else:
        raise NotImplementedError(data_name)
    
    return dataset


if __name__ == "__main__":
    examples = load_data("gpqa")
    print('test')
