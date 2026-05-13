# A bird's eye view on informed classification

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
Neurosymbolic AI is a growing field of research aiming to combine neural network learning capabilities with the reasoning abilities of symbolic systems. In this paper, we tackle informed classification tasks, i.e. multi-label classification tasks informed by prior knowledge that specifies which combinations of labels are semantically valid. Several neurosymbolic formalisms and techniques have been introduced in the literature, each relying on a particular language to represent prior knowledge. We take a bird's eye view on informed classification and introduce a unified formalism that encapsulates all knowledge representation languages. Then, we build upon this formalism to identify several concepts in probabilistic reasoning that are at the core of many techniques across representation languages. We also define a new technique called semantic conditioning at inference, which only constrains the system during inference while leaving the training unaffected, an interesting property in the era of off-the-shelves and foundation models. We discuss its theoritical and practical advantages over two other probabilistic neurosymbolic techniques: semantic conditioning and semantic regularization. We then evaluate experimentally and compare the benefits of all three techniques on several large-scale datasets. Our results show that, despite only working at inference, our technique can efficiently leverage prior knowledge to build more accurate neural-based systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a unified formalism that encapsulates learning and inference in the presence of prior knowledge specified in propositional logic, also known as neurosymbolic AI. Using the presented formalism, they are able to delineate the approaches present
in the literature, and define a new technique which they call *semantic conditioning at inference*. The proposed method applies to the
neural network only during inference, and does not impose any changes during training.

### Strengths
- The paper is pretty well written, and provides a comprehensive overview of the different neurosymbolic approaches in the literature

- The proposed approach, *semantic conditioning at inference*, greatly boosts the accuracy of the models on the tasks considered
in the experimental section, while at the same time avoiding the computational costs of performing MAP inference on the full distribution.

### Weaknesses
 - While the paper provides a nice, unifying overview of the field and the key techniques developed, I am not quite sure that such a view is especially novel

- Furthermore, and perhaps more crucial, is that other work such as that by Niepert et al and Pogancic et al, as well as other works using combinatorial solvers do exactly what the authors set out to do: compute the MPE state at inference time without maintaining the distribution over the entire space of outputs, thereby also avoiding the often prohibitive task of counting, and which the authors do not compare to. This is my biggest concern, as it puts into question the novelty of the authors' technical contributions.

- In the experimental section, I initially found it hard to parse the Figure 2 due to the absence of an explicit mention of what the acronyms used stand for.

### Questions
Please see the weaknesses section.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper takes a neurosymbolic AI approach to multi-label classification where constraints of the output space are imposed using a propositional language and these constraints are accounted for when making predictions. It provides extensive background material on the formalisms that the method employs and evaluates on some multi-label classification benchmarks, demonstrating that accounting for these constraints outperforms not accounting for them.

### Strengths
I appreciate that your paper employs techniques that are not particularly popular in mainstream ML. It's great to bring exposure to alternative ideas.

### Weaknesses
One challenge of employing techniques that are less familiar to readers is that the paper needs to set up a significant amount of background material. This occupies the majority of the paper. Some of the content is fairly elementary, such as explaining how to use a differentiable loss function to learn a probabilistic classifier.

The experiments are not particularly rigorous. I would have appreciated more ablations analyzing, for example, the impact of different algorithmic choices. For example, what fraction of predictions actually violate the constraints for the baseline model? There is also no benchmarking against other approaches to multi-label classification from prior works that go beyond independent prediction across labels.

### Questions
It's important to bridge the gap between the neurosymbolic AI community and related ideas that have previously appeared in other parts of the literature. A significant missing piece in the discussion of related work is anything regarding probabilistic graphical models, which are based on similar formalisms as section 2.

Based on some quick background reading, here are some key multi-label classification papers that did inference in undirected graphical models: 

Ghamrawi, Nadia and McCallum, Andrew. Collective multi-label classification.
Finley, Thomas and Joachims, Thorsten. Training structural svms when exact inference is intractable.
Meshi, Ofer, Sontag, David, Globerson, Amir, and Jaakkola, Tommi S. Learning efficiently with approximate inference via dual losses
Petterson, James and Caetano, Tiberio S. Submodular multi-label ´ learning.

Can you please discuss more directly the relationship to PGMs? For the particular problem setups you use, is there a corresponding formulation as a PGM?

=========
I had a hard time understanding the complexity of the actual prediction problems. It would have been great if you had compressed some of the background and instead provide concrete details about the structure of the constraints in each problem that is considered in the experiments and how inference wrt these constraints is handled. I know some of these are provided in the appendix. Can you provide a high-level summary here, such that such a summary could be included in the main paper?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
### Paper Summary
The authors introduce syntax/formalism(s) that bridge a number of works interested in informed classification.

The authors find that simplifying Semantic Conditioning (SC) to Semantic Conditioning at Inference (SCI) captures 75% of the improved performance gain. This is particularly valuable because it suggests that we can flexibly use existing models without additional training!

### Reviewer's Note
I am not an expert in neurosymbolic systems. I have read some of these papers, but this not an area of my direct expertise, so it is possible I am missing something.

### Review Summary
The authors argue that introducing the additional syntax does is a contribution in-and-of-itself, but I don't (yet) agree. The shared syntax does not seem to illustrate/highlight/show something new. I would expect that the authors of the mentioned previous works would agree that a shared syntax could be devised across problems, but instead chose to use the most apt approach for their respective formulations. I do think that it may be useful, if it leads to new developments/understandings, but the formalism itself only seems like 1/2 of a contribution. 

(I am quite open to discussion on this point or alternative perspectives.)

This leaves the primary contribution of this paper being: Removing part of an existing method only partially reduces performance. This is good to know, but I'm not sure its critical. Another way of looking at this is that I think the paper spends a lot of energy/time presenting this new syntax but I don't think we (the reader/the field) is getting a lot out of this, and the contribution of SC --> SCI is not particularly/directly related to the syntax.

### Strengths
* The paper does a great job of providing a lot of background and previous work. 
    * So much so that this paper feels mostly like an expositionary piece. If ICLR is interested in exposition-only work (somewhat like a focused survey) and the paper were slightly modified to pull this forward, then I would find the work more compelling. (I don't think that this is the case?)

### Weaknesses
The main weakness, in my view, is that the paper only makes a small and incremental contribution. Claiming that "semantic conditioning at inference" is a new technique is somewhat of a stretch. It is essentially an ablation of the full semantic conditioning method. 

The other claimed contribution is that the paper provides a unified formalism. To claim this as a contribution is questionable. The paper could easily have used propositional logic as the underlying framework and then have made the point that other propositional languages can be treated similarly. The current formulation also has the drawback of making the notation heavy and the explanations more opaque.  

Some minor points:

The last paragraph before section 4.1 (on fuzzy logics) feels out of place, and similar for the first paragraph of Section 4.1. The whole built-up of the framework has assumed probabilistic reasoning, so it seems weird to suddenly justify this choice in the middle of the paper.

Typo in the abstract: theoritical 

Figure 2: please add explanations for the different acronyms (SCI, IMC, etc) to the caption, even though their meaning can be guessed.

### Questions
What did the new syntax exactly offer/contribute to your understanding/method/results? Am I missing or misunderstanding something?

While the background is already taking up a lot of the paper, finding space to provide key examples of the type of data you're working with could help get the reader to quickly track what you want to investigate. 

Relatedly, what errors does SCI make that SC doesn't? Can you provide examples of this?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper makes two related contributions:

* First, the paper proposes a general framework for encoding prior knowledge, within the context of probabilistic neurosymbolic approaches for multi-label classification.
* Second, the paper proposes a variant on existing methods for  probabilistic neurosymbolic multi-label classification. Specifically, while in existing work, semantic conditioning is applied both at training time and at inference time, the authors propose to do this only at inference time. This has the advantage of making the method much more efficient, while experimental results show that the penalty for doing this only at inference time is (at worst) limited.

### Strengths
The paper is carefully written and proposes a clean formalisation of probabilistic neurosymbolic multi-label classification. The formulation clearly illustrates the differences between two important previous techniques: semantic regularization and semantic conditioning.

The fact that performing semantic conditioning only at inference time does not deteriorate the performance much is a useful finding, which is worth highlighting to practitioners.

### Weaknesses
The main weakness, in my view, is that the paper only makes a small and incremental contribution. Claiming that "semantic conditioning at inference" is a new technique is somewhat of a stretch. It is essentially an ablation of the full semantic conditioning method. 

The other claimed contribution is that the paper provides a unified formalism. To claim this as a contribution is questionable. The paper could easily have used propositional logic as the underlying framework and then have made the point that other propositional languages can be treated similarly. The current formulation also has the drawback of making the notation heavy and the explanations more opaque.  

Some minor points:

The last paragraph before section 4.1 (on fuzzy logics) feels out of place, and similar for the first paragraph of Section 4.1. The whole built-up of the framework has assumed probabilistic reasoning, so it seems weird to suddenly justify this choice in the middle of the paper.

Typo in the abstract: theoritical 

Figure 2: please add explanations for the different acronyms (SCI, IMC, etc) to the caption, even though their meaning can be guessed.

### Questions
For the experiments, the only baseline is to use an uninformed model. At least, I would have expected something like fuzzy regularization there as well.

### Soundness
4

### Presentation
3

### Contribution
1
