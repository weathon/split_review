# CtD: Composition through Decomposition in Emergent Communication

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Compositionality is a cognitive mechanism that allows humans to systematically combine known concepts in novel ways.
This study demonstrates how artificial neural agents acquire and utilize compositional generalization to describe previously unseen images.
Our method, termed \`\`Composition through Decomposition'', involves two sequential training steps.
In the \'Decompose\' step, the agents learn to decompose an image into basic concepts using a codebook acquired during interaction in a multi-target coordination game.
Subsequently, in the \`Compose\' step, the agents employ this codebook to describe novel images by composing basic concepts into complex phrases.
Remarkably, we observe cases where generalization in the `Compose' step is achieved zero-shot, without the need for additional training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces "Composition through Decomposition" (CtD), an approach enabling artificial neural agents to achieve compositional generalization by breaking down and recomposing concepts. CtD consists of two phases: in the "Decompose" step, agents learn to identify basic concepts in images through a codebook-based communication setup; in the "Compose" step, they use these learned concepts to describe novel images. This structured approach allows for zero-shot generalization to unseen compositions. Experimental results on multiple datasets show CtD can outperform standard methods, achieving high accuracy and compositionality.

### Strengths
The approach of "Composition through Decomposition" (CtD) method stands out as a two-step approach where agents first learn to decompose complex objects into simpler concepts before recomposing them. It is an interesting way to get agents to perform compositional inference.

Using a discrete codebook to handle basic concept representations is well-grounded, showing the potential for generalization without additional training. This idea, inspired by linguistic encoding methods, enables efficient compositional representation and surpasses traditional methods in performance on multiple metrics.

The paper evaluates the CtD approach across diverse datasets (e.g., THING, SHAPE, MNIST), demonstrating high accuracy and compositionality scores. The performance evaluation using zero-shot and multi-target settings strengthens the claim that CtD enables compositional generalization.

The authors us multiple metrics (e.g., AMI, CBM, BOS) to give a clear picture of the model's strengths and weaknesses.

I generally thought this paper was well-written and the presentation was good.

### Weaknesses
Several methods have been proposed and evaluated during recent years by the
emergent communication (EC) research community..." -> isn't meta-learning another one to mention here?

"Notably, our method achieves extremely high performance, characterized by perfect accuracy and
compositionality, on multiple datasets." -> just say it achieves perfect accuracy, no need to say extremely high

"we assert that before effectively composing basic concepts into complex ones, agents must acquire the ability
to decompose complex concepts into basic ones" -> must sounds quite strong here. Do you really show that there is no other way to do this? Or is your method one way to accomplish compositionality?

You're using "employed" a lot when really you could just say "use"

I didn't get how the beta of the loss function (game and codebook-tradeoff) was set at first but later it said that the authors "experimented with various values of β1 and β2, ranging from 0.1 to 1.0 and found no significant difference in results." What do you make of this? Why does it not make a big difference? Is this because the loss is dominated by one part in any case?

There is a lot of things going on in Figure 3. Why are there arrows in there? This seems to mostly just show exactly what is in the text already.

I like the ablation studies although it could be a bit better explained why multi-target makes a difference and how the differences between the data sets in this ablation can be explained.

The paper discusses a multi-loss optimization, but the complexity and potential sensitivity of the CtD approach to hyperparameter settings (e.g., β1 and β2 values) could make it less accessible for broader use. 

For some datasets, such as COCO, the author found limited compositional performance but this wasn't really discussed any further.

I didn't fully get why zero-shot is better than further training in MNIST. The authors say this is because of the difficulties of further training, but why?

The initialization of the code book is a very interesting observation. So how would one set this appropriately in practice to make sure it's successful? Should it always match the number of basic concepts?

### Questions
I didn't fully get why zero-shot is better than further training in MNIST. The authors say this is because of the difficulties of further training, but why?

The initialization of the code book is a very interesting observation. So how would one set this appropriately in practice to make sure it's successful? Should it always match the number of basic concepts?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This study presents "Composition through Decomposition" (CtD), a method that enables artificial neural agents to achieve compositional generalization, allowing them to describe new images by systematically combining learned basic concepts. CtD involves two stages: first, a “Decompose” step where agents learn to break down complex images into discrete basic concepts using a codebook developed through multi-target coordination games. Then, in the “Compose” step, agents use this codebook to describe novel images by recombining basic concepts, achieving zero-shot generalization in some cases.

### Strengths
Originality: Fairly original, builds upon previous work but with somewhat novel contributions

Quality: Very pertinent experiments on a wide range of tasks with a wide range of metrics

Clarity: Sections 1, 2, 4, 5, 6, and 7 are very clear and well written

Significance: Significant contribution to understanding how compositionality can emerge in a learning system, which is an important concept to understand faster and more effective learning

### Weaknesses
1. It seems to me that in order to properly do the CtD approach, you need to already know the concepts you want to compose ahead of time in order to setup the 2 phases of training. I don't know how realistic this is in real-world settings.

2. I think the paper should make it clear what the novel part of the work is (from what I understand it is only the 2 phases of training), because now it seems like all 3 parts of section 3 are novel

### Questions
My questions are based on the weaknesses listed above:

Could the authors discuss potential methods for automatically discovering or learning relevant concepts during the decomposition phase? How might this approach be modified for real-world applications where predefined concepts are not available?

Could the authors add a paragraph in Section 3 or in the introduction that clearly outlines the key innovations of their approach? This would help readers better understand which components are novel and which build upon previous work

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies how to improve the model’s compositional generalization ability. Specifically, the authors propose a two-stage training pipeline, in which the model first learns to decompose an image into basic concepts using a codebook and then recombines the learned features to describe novel concepts. The experiments on different image datasets showcase that the proposed method indeed improves the model’s ability compared with other baselines. However, the proposed method needs a carefully selected training set, which limits its applicability to more practical scenarios. Also, the paper hasn’t discussed an important line of work related to this problem, i.e., iterated learning, which is a multi-generation-based training pipeline that can amplify the inherent bias towards compositional mappings automatically. I guess combining the method proposed in this paper and multi-generation training can further improve the model’s ability on compositional generalization. In summary, I think the paper has the potential, but due to the reasons above, I would like to give a negative score for the current version.

### Strengths
- The presentation is good, and the paper is easy to follow.
- The experiments are well conducted, covering both toy data and real images.
- The conclusions drawn from the experiments are inspiring. (E.g., I like the results in Figure 3.)
- The zero-shot results are interesting.

### Weaknesses
 - The paper doesn't mention the multi-generation-based approach for the compositional generalization problem. Actually, the two-stage training proposed here can also be analyzed using similar theoretical tools provided in related works, e.g., [3]. Furthermore, [1] also studies the compositional generalization problem in the context of emergent communication, which is identical to the one studied in this paper. Such an iterated training fashion has proven to be effective in many other fields, e.g., molecular graph prediction [3], visual VQA [2], large VLM like CLIP [4], etc. It might be helpful to discuss (or even compare) with methods in this line of work. So, providing more discussions about the potential synergies or tradeoffs between the decomposition-composition approach and multi-generational training would make the paper stronger.
- The discussions and analysis throughout the paper are high-level. A more in-depth discussion of the dataset selection design in different phases would make the paper stronger. For example, the authors mentioned in line 190 that “In the DECOMPOSE step all targets share a phrase composed from exactly one FVP”, what will happen if this assumption is violated? How will it influence the final results? Will the network be robust enough when this assumption is mildly violated? Since this assumption is too strong to be true in many practical scenarios, relying too much on this assumption might harm the contribution of the paper. I believe conducting ablation studies where the single-FVP assumption is systematically relaxed to varying degrees would make the paper stronger.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3
