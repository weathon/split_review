# Chain-of-Jailbreak Attack for Image Generation Models via Editing Step by Step

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Text-based image generation models, such as Stable Diffusion and DALL-E 3, hold significant potential in content creation and publishing workflows, making them the focus in recent years.
Despite their remarkable capability to generate diverse and vivid images, considerable efforts are being made to prevent the generation of harmful content, such as abusive, violent, or pornographic material.
To assess the safety of existing models, we introduce a novel jailbreaking method called Chain-of-Jailbreak (CoJ) attack, which compromises image generation models through a step-by-step editing process.
Specifically, for malicious queries that cannot bypass the safeguards with a single prompt, we intentionally decompose the query into multiple sub-queries. The image generation models are then prompted to generate and iteratively edit images based on these sub-queries.
To evaluate the effectiveness of our CoJ attack method, we constructed a comprehensive dataset, CoJ-Bench, encompassing nine safety scenarios, three types of editing operations, and three editing elements.
Experiments on four widely-used image generation services provided by GPT-4V, GPT-4o, Gemini 1.5 and Gemini 1.5 Pro, demonstrate that our CoJ attack method can successfully bypass the safeguards of models for over 60\% cases, which significantly outperforms other jailbreaking methods (i.e., 14\%).
Further, to enhance these models' safety against our CoJ attack method, we also propose an effective prompting-based method, Think Twice Prompting, that can successfully defend over 95\% of CoJ attack.
We release our dataset\footnote{https://docs.google.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the "Chain-of-Jailbreak" (CoJ) attack, a method to bypass safeguards in text-based image generation models like GPT-4V and Gemini 1.5. By breaking down malicious queries into harmless sub-queries and using iterative editing, CoJ can generate harmful content that would otherwise be blocked. The study highlights significant vulnerabilities in current models, achieving a 60% success rate in bypassing safeguards. To counter this, the authors propose "Think Twice Prompting," a defense strategy that prompts models to internally evaluate the safety of the content before generation, successfully defending against 95% of CoJ attacks.

### Strengths
Innovative Methodology: The introduction of the Chain-of-Jailbreak (CoJ) attack is a significant advancement. By decomposing malicious queries into harmless sub-queries and using iterative editing, the paper presents a novel approach to bypassing safeguards in text-based image generation models.

Comprehensive Evaluation: The authors have conducted extensive experiments across multiple models (GPT-4V, GPT-4o, Gemini 1.5, and Gemini 1.5 Pro) and scenarios. This thorough evaluation demonstrates the robustness and effectiveness of the CoJ attack, achieving a high success rate of 60%.

Proposed Defense Mechanism: The paper doesn't just identify vulnerabilities but also proposes a practical solution. The "Think Twice Prompting" defense strategy, which prompts models to internally evaluate the safety of the content before generation, shows a high defense success rate of 95%.

### Weaknesses
Method Robustness: The authors propose using Edit Operations and Edit Elements to break down a malicious query into sub-queries. In the implementation, they manually apply this approach to five seed queries and leverage a large language model (LLM) to generalize these examples to other queries. However, my concern is whether the model consistently adheres to the principles of the proposed Edit Operations and Edit Elements. It would be helpful if the authors could elaborate on the reliability of this approach.

Number of Sub-Queries: As illustrated in Figure 1, the malicious query is divided into three sub-queries. This raises the question of how many sub-queries would be optimal for other queries. Is there a “best” decomposition, and how can it be identified? While the authors rely on an LLM for this task, I am concerned about the LLM’s ability to consistently find the optimal decomposition.

Choice of LLM: The authors specify using Mistral-Large-2 for modifying malicious queries automatically. It would be informative to know whether other models were considered and if similar performance could be achieved with smaller models requiring less computational power. This consideration is especially relevant for attackers with limited resources who may not have access to high-powered computational hardware.

### Questions
1. How reliably does the model follow Edit Operations and Edit Elements across queries?

2. What is the optimal number of sub-queries, and can the LLM consistently find it?

3. Were other models tested, and can similar results be achieved with less computationally intensive options?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a method to make text-to-image models generate images with harmful content. The harmful image is defined as an image with harmful words in it. The idea is to decompose the prompt into multiple sub-queries, which gradually generate a harmful image. A benchmark of queries for such harmful images are also collected and used for evaluation.

### Strengths
Safety of text-to-image models is an important topic. 

A method is proposed to generate a specific type of harmful images. 

A benchmark is collected.

### Weaknesses
The scope is a little bit limited. Only images with harmful words can be generated by this method. This should be made clear from paper title and abstract. 

To generate such images, more straightforward approach may be applicable. E.g., directly merge harmful words with images. Note that, an attacker jailbreaks a GenAI model to generate harmful images, and still needs to propagate them to cause real harms for other people. To generate the types of harmful images considered in this work, an attacker may not need a text-to-image model and thus may not need the proposed attack. 

Comparison with baseline methods is missing. What are the alternative approaches to generate such harmful images? Does the attacker have to use a text-to-image model? Even if text-to-image model is needed, any other baseline methods can be used to generate such harmful images? It is not clear in the current paper.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel method called Chain-of-Jailbreak (CoJ) attack that bypasses safeguards in image generation models. The method proposes a decomposition method that breaks down malicious prompts into a series of sub-queries. The experiments demonstrate that such a method is able to jailbreak open-source black-box models like GPT-4V, GPT-4o, and Gemini 1.5 by generating harmful contents in various malicious categories. The authors also introduce a dataset named “CoJ-Bench”, which consists of various jailbreaking prompts in a wide range of safety scenarios. The paper claims to achieve high jailbreak success rates (~60%), which outperforms traditional prompt-based attacks. In addition, the authors introduce a defense mechanism against the proposed attack called “Think Twice Prompting”, which asks the model to check the safety implications once more before generating the images.

### Strengths
1. The paper proposes a novel yet simple approach to bypass image generation model safeguards, which are known to be built stronger than open-source models such as Stable Diffusion. It also demonstrated a huge outperformance against previous jailbreaking methods in text-to-image generation. 

2. The paper also introduces the edit operation in the decomposition process is structured systematically rather than simply tokenizing the input prompt. The diversity of the attack method showed the effectiveness of jailbreaking these models.

3. The CoJ benchmark covers a wide range of safety scenarios, with an even more detailed division in the subgroups of each safety category of the benchmark, which enhances reproducibility and evaluation standards.

### Weaknesses
1. The defense method is not clearly explained and not realistic enough. How and when are the defense prompts inputted to the image generation? The proposed 'Think Twice Prompting' lacks specific implementation details, such as the exact phrasing of the prompts and how they interact with the model's internal mechanisms. It's unclear if these prompts are prepended, appended, or integrated within the original prompt, and how this affects the model's attention and generation process. Furthermore, the defense seems overly simplistic and might be easily bypassed by slightly more sophisticated adversarial attacks. The paper does not explore the robustness of this defense against variations in the attack strategy.

2. A threat model of this type of attack is not specified. When are these attacks be utilized in a real-life scenario? The paper lacks a detailed discussion on the practical implications of this attack. It does not specify the potential real-world scenarios where such attacks could be deployed, nor does it discuss the potential impact of such attacks on users or systems. Without a clear threat model, it is difficult to assess the true significance of the proposed attack method and its potential for misuse.

3. The traditional attack methods are not cited as well as not explained in the background section. The paper does not provide a comprehensive overview of existing jailbreaking techniques for text-to-image models. This lack of context makes it difficult to understand the novelty and significance of the proposed method. A more thorough discussion of the existing landscape of adversarial attacks would be beneficial.

### Questions
1. What could be the reason behind why “Insertion-then-Delete” is the most effective attack? In general, why was decomposition effective compared to traditional attack methods?

2. The traditional attack methods are not cited as well as not explained in the background section.

3. In the automatic evaluation, what is the purpose of observing the response of LLM? How does GPT-4 responding No indicate that the image generation models not refusing the malicious query?

### Soundness
2

### Presentation
3

### Contribution
2
