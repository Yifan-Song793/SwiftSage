# 🤖 SwiftSage: A General Reasoning Framework with Fast and Slow Thinking

> [!IMPORTANT]
> This is the beta version of SwiftSage V2, which is still under development. The current version may not be stable and is subject to change. Any comments and suggestions are welcome! 
> The code of SwiftSage V1 (for the experiments in NeurIPS 2023) is archived in the [`science_world`](https://github.com/SwiftSage/SwiftSage/tree/science_world) branch.


<!-- Github Readme Important Callout box note -->
## 🔗 Links:
- Gradio Demo on HuggingFace: https://hf.co/spaces/swiftsage-ai/SwiftSage
- Get your API key: [Together AI](https://www.together.ai), [SambaNova](https://www.sambanova.ai), etc.
- Previous paper (NeurIPS 2023 Spotlight): https://arxiv.org/abs/2305.17390 
- Core contributors for v2: [Bill Yuchen Lin](https://yuchenlin.xyz/), [Yifan Song](https://scholar.google.com/citations?user=b_HfZhQAAAAJ&hl=en), .... 

## Installation

```bash
pip install git+https://github.com/SwiftSage/SwiftSage.git  
# alternatively, you can clone the repo and install it locally
# git clone https://github.com/SwiftSage/SwiftSage.git
# pip install -e .
```

## Usage

```bash
export TOGETHER_API_KEY="your-api-key" # get your key from https://www.together.ai
swiftsage --problem "How many letter r are there in 'My strawberry is red.'?"
```

Check more configurations in the code: [swiftsage/cli.py](swiftsage/cli.py).

## Design of SwiftSage V2 

The key motivation of SwiftSage is to provide a general reasoning framework that can mimic the fast and slow thinking processes in human cognition. The fast thinking process is based on the intuition and heuristic reasoning, while the slow thinking process is based on more analytical, critical thinking. Unlike SwiftSage V1, which relies on feedbacks from the well-designed environment such as ScienceWorld, SwiftSage v2 is designed to be more general and can be applied to various reasoning tasks. 

**General reasoning.** In order to support more general reasoning, we also use [Agent Lumos](https://arxiv.org/abs/2311.05657)'s idea to unify the task formats with a plan-ground-execute paradigm. We define actions as generating a python code snippet. 

**In-context reinforcement.** Instead of [behavior cloning SFT](https://arxiv.org/abs/2311.05657) and [trajectory optimization](https://arxiv.org/abs/2403.02502), we focus on prompting-based strategies to achieve the same goal such that it is easier to adapt to newer models and API-based LLM access. The feedbacks are generated by LLMs and are used as reflections and rewards for SwiftSage to update reasoning strategies.

### SwiftSage Components

The main components in SwiftSage v2: 
- **Swift Agent**: A smaller LM that generates python code snippets based on the prompt.
- **Feedback Agent**: A larger LM that generates feedbacks based on the prompt and the generated code snippet.
- **Sage Agent**: A reasoning agent that uses the feedbacks to update the reasoning strategies.
- **Retriever** (soon to be added): A retrieval module that retrieves the most relevant feedbacks for the current prompt.
- **Executor**: A python executor that executes the generated code snippets.


### SwiftSage Workflow

- Step 1. Given a reasoning problem that a user inputs, Swift Agent firsts generates a plan and a code-based solution. 
- Step 2. The executor executes the code snippet and generates the final answer. 
- Step 3. We then use the feedback agent to analyze the generated answer and provide feedbacks including a short paragraph and a score. Depending on the score and the threshold, we can decide if the current solution is good enough to show to the user. 
    - Case 3.1. If yes, we then stop the process and show the answer to the user.
    - Case 3.2. If not, we use the critical feedbacks to prompt the Swift Agent again to generate a new solution based on the feedbacks. Go to Step 1 with the feedbacks as the new prompt.
    - Case 3.3 If the new solution is still not good enough after a few iterations, go to Step 4.
- Step 4. If smaller models cannot solve the task, we can then use the Sage Agent to solve the problem in a more analytical way, and then provide the final answer to the user.

TODO: Soon, we'll add retrieval augmentation step to further improve the reasoning process of Swift Agent.  



## Misc.

### Contact

Please email [Bill Yuchen Lin](https://yuchenlin.xyz) at the [gmail](yuchenlin1995@gmail.com) address.

### License
We use the MIT license for SwiftSage.

### Citation 
The technical report of SwiftSage V2 is under preparation. Please cite the following paper for the previous version of SwiftSage: 
```bib
@inproceedings{
  lin2023swiftsage,
  title={SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks},
  author={Bill Yuchen Lin and Yicheng Fu and Karina Yang and Faeze Brahman and Shiyu Huang and Chandra Bhagavatula and Prithviraj Ammanabrolu and Yejin Choi and Xiang Ren},
  booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
  year={2023}
}
```

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=SwiftSage/SwiftSage&type=Date)](https://star-history.com/#SwiftSage/SwiftSage&Date)