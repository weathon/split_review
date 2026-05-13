# Pretrained Hybrids with MAD Skills

- Decision: Reject
- Scores: 6, 3, 5

## Abstract
While Transformers underpin modern large language models (LMs), there is a growing list of alternative architectures with new capabilities, promises, and tradeoffs.
  This makes choosing the right LM architecture challenging. 
  Recently-proposed  \emph{hybrid architectures} seek a best-of-all-worlds approach that reaps the benefits of all  architectures. 
  Hybrid design is difficult for two reasons: it requires manual expert-driven search, and new hybrids must be trained from scratch. 
  We propose \textbf{Manticore},\footnote{The Manticore is a fearsome human/lion/scorpion hybrid from Persian mythology.} 
  a framework that addresses these challenges. 
  Manticore \textit{automates the design of hybrid architectures} while reusing pretrained models to create \textit{pretrained} hybrids. 
  Our approach augments ideas from differentiable Neural Architecture Search (NAS) by incorporating simple projectors that translate features between pretrained blocks from different architectures. 
  We then fine-tune hybrids that combine pretrained models from different architecture families---such as the GPT series and Mamba---end-to-end. 
  With Manticore, we enable LM selection without training multiple models, the construction of pretrained hybrids from existing pretrained models, and the ability to \emph{program} pretrained hybrids to have certain capabilities. 
  Manticore hybrids outperform existing manually-designed hybrids, achieve strong performance on Long Range Arena (LRA) tasks, and can improve on pretrained transformers and state space models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper builds by proposing a new framework for automating the design of hybrid language models by re-using existing pre-trained models using ideas from Neural Architecture Search. The authors show that their approach allows for merged language models to be competitive with their component models and also outperform them on fine-tuning tasks.

### Strengths
1. The paper is well-written and the the motivation is clear and convincing.
2. The figures are well-designed and helpful.
3. Interesting results that prove the effectiveness of their framework on specific models.

### Weaknesses
1. The experiments done are mostly on smaller models and it's not clear if MAD remains effective with larger models. The authors could do additional experiments with other open-source models to validate this.


### Questions
1. Have you done experiments to validate whether the performance continues to hold at scale?
2. What is the overhead of the projectors?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces Manticore, a framework for creating hybrid architectures by combining pretrained components from different language models (LMs). Manticore aims to automate hybrid model design by reusing pretrained model components from distinct architectures, such as Transformers and state-space models, using projectors to align feature representations between these models. The framework's goal is to merge model architectures in a way that preserves their respective strengths, ideally achieving better performance than the individual components. Through experiments on the Long Range Arena (LRA) and MAD tasks, Manticore demonstrates comparable or improved performance over some individual models and existing hybrid models.

### Strengths
+ Manticore’s approach to combining pretrained models from different architectures using projectors and mixture weights is innovative and extends beyond typical model merging methods.
+ Manticore’s design, which allows for fine-tuning and programming pretrained hybrids, offers a degree of flexibility, making it potentially beneficial for practitioners looking to leverage diverse model architectures.
+ Testing across LRA and MAD tasks provides an initial sense of the framework's potential, although the evaluation depth limits the conclusions drawn.

### Weaknesses
 - The main claim, "Pretrained hybrids can outperform their component models on fine-tuning tasks," is not well-supported. A fair comparison would entail fine-tuning Manticore and its component models under the same budget to evaluate relative gains. Without this, it’s unclear whether the hybrid approach provides substantial benefits beyond those of individually optimized models.
- Manticore requires a dedicated training process for projector layers and mixture weights, potentially adding overhead and limiting applicability in constrained environments.
- The absence of publicly available code restricts reproducibility and verification of the results, limiting the community's ability to assess the framework’s impact fully.

### Questions
1. How would Manticore perform relative to its component models if they were fine-tuned under the same computational budget? Would this comparison validate Manticore’s primary claim of outperforming its component models?
2. Could the authors elaborate on the memory and computational efficiency of Manticore hybrids, especially compared to traditional single-model architectures? Does the use of projectors introduce significant overhead?

### Soundness
2

### Presentation
2

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
Manticore is a framework for automating the creation of hybrid language model architectures by reusing pre-trained models from different architectures. By leveraging NAS and projectors, Manticore enables pre trained hybrid models that combine the strengths of multiple architectures, allowing for flexible and high-performing LLMs without extensive manual design or retraining.

### Strengths
This paper focuses on an important and relevant problem of using architectural components from different state-of-the-art model architectures to construct a hybrid model that provides the best of all worlds without incurring expensive pre-training and search space exploration overheads.

It introduces a novel idea of projectors that enable different architectures to interact in each other feature space by projecting an intermediate shared feature space that acts as a translator for them.

### Weaknesses
Although the idea of projectors is novel but using gating to combine the contributions of different architectures has been explored in Mixture of experts [1], weighted ensemble averaging and finds a direct use in this paper.

The evaluation compares the combined hybrid that has 2x the number of parameters and >2x FLOPs due to projectors and gating against individual models of half the size.

In Table 1, Mamba is already better than Pythia in all of the tasks, in Table 2, Mambaformer is also better in all tasks but one, In Table 4, GPT-Neo is better than all tasks, So creating a hybrid is achieving almost the same score as the better model.

### Questions
A fair comparison would either be a model of the same architecture with 2x size or the hybrid being discretized and having the same amount of FLOPs/parameters of the one of the individual models. This would address weakness 2.

 A stronger test would be to consider models that perform better in some tasks than others and then validate if the hybrid does achieve the best of both worlds. This would address the weakness 3.

### Soundness
3

### Presentation
4

### Contribution
3
