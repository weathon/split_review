# Super(ficial)-alignment: Strong Models May Deceive Weak Models in Weak-to-Strong Generalization

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Superalignment, where humans act as weak supervisors for superhuman models, has become a crucial problem with the rapid development of Large Language Models (LLMs). 
Recent work has preliminarily studied this problem by using weak models to supervise strong models, and discovered that weakly supervised strong students can consistently outperform weak teachers towards the alignment target, leading to a \textbf{weak-to-strong generalization} phenomenon. 
However, we are concerned that behind such a promising phenomenon, whether there exists an issue of \textbf{weak-to-strong deception}, where strong models deceive weak models by exhibiting well-aligned in areas known to weak models but producing misaligned behaviors in cases weak models do not know. 
We take an initial step towards exploring this security issue in a specific but realistic multi-objective alignment case, where there may be some alignment targets conflicting with each other (e.g., helpfulness v.s. harmlessness). 
We aim to explore whether, in such cases, strong models might deliberately make mistakes in areas known to them but unknown to weak models within one alignment dimension, in exchange for a higher reward in another dimension. 
Through extensive experiments in both the reward modeling and preference optimization scenarios, we find: (1) The weak-to-strong deception phenomenon exists across all settings. (2) The deception intensifies as the capability gap between weak and strong models increases. (3) Bootstrapping with an intermediate model can mitigate the deception to some extent, though its effectiveness remains limited. 
Our work highlights the urgent need to pay more attention to the true reliability of superalignment.}~\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores the phenomenon of weak-to-strong deception, where strong AI models supervised by weaker models can appear aligned in familiar areas while misaligning strategically in areas unknown to the weak model. Through experiments with large language models, the authors demonstrate that this deception increases with the capability gap between weak and strong models, especially under conflicting alignment objectives (like helpfulness vs. harmlessness). While some mitigation methods, like high-confidence filtering and bootstrapping, show limited effectiveness, the paper underscores an urgent need for more reliable supervision.

### Strengths
1. Originality: The paper introduces the novel concept of "weak-to-strong deception," which is an underexplored alignment issue where strong models exploit gaps in weak supervision by selectively misaligning in unknown areas. 

2. Quality: The research is methodologically strong, with diverse experimental settings involving various large models (e.g., GPT-2, OPT, Mistral, LLaMA) across reward modeling and preference alignment tasks. The introduction of a "Deception Score" and structured definitions for knowledge boundaries is interesting. Balanced discussions on the limitations of mitigation techniques (e.g., high-confidence filtering, bootstrapping) are also helpful. 

3. Clarity: The paper is well-organized, with clear definitions and diagrams that help understand the dynamics between weak and strong models. Concepts like knowledge spaces and the Deception Score are well explained, making complex ideas easy to understand.

4. Significance: The study’s findings are significant for AI alignment, particularly as they highlight vulnerabilities in supervising increasingly powerful AI models. The weak-to-strong deception phenomenon underscores the need for improved supervision techniques in high-stakes applications, with implications for ethical AI and safety. 

In summary, the paper’s originality in framing weak-to-strong deception, the quality and breadth of its experimental design, its clear presentation, and its implications for alignment make it a good contribution to the field.

### Weaknesses
1. Synthetic scenarios used for controlled testing may not capture real-world complexities. Having interactive, dynamic environments (e.g., feedback systems) would improve generalizability. Did the authors consider testing with more complex, real-world environments?
2. The use of static thresholds to identify deception risks seems somewhat limiting. A dynamic thresholding or sensitivity analysis could be a better alternative.
3. Techniques like high-confidence filtering and bootstrapping show limited effectiveness in reducing deception. Exploring adaptive or meta-learning approaches may yield better solutions?
4. By focusing primarily on "harmlessness," the study seems a bit narrow, and other alignment goals (e.g., "honesty," "fairness") could improve generalizability.

### Questions
See above in weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper considers the problem of weak-to-strong generalization and shows a particular kind of vulnerability, where the strong model regresses a dimension that the weak model cannot capture while getting better rewards in another dimension where the weak model can capture. In other words, they study a very specific kind of reward hacking that occurs in the context of weak to strong generalization and discuss the pitfalls in this paradigm.

### Strengths
+ The paper considers a very important problem that is increasingly relevant in aligning frontier models where to preferences where the source of preference can often be weaker than the model itself. It showcases a specific type of reward hacking in the context of helpfulness vs harmlessness spectrum. 

+ The results are well justified and analyzed. Although the results are preliminary, the paper considers a concrete setting where its able to show the clear tradeoff the strong model makes. Using a bunch of small models, they systematically analyze the effects.

### Weaknesses
The main weakness of this paper I find is the lack of relationship to reward hacking behavior that is common in LLM alignment. For example, it is well known that LLMs tend to fool the reward models by creating artifacts that make the reward model very good on style and getting increased score, while reducing its efficiency in core capability (e.g., instruction following). Although the phenomenon studied here is posited differently, there are similarities which the paper does not make the connection towards. The paper does not sufficiently explore the nuances of reward hacking, particularly how models might exploit weaknesses in the reward signal to achieve high scores without genuinely improving on the intended objective. Specifically, the paper's analysis could benefit from a more detailed comparison to scenarios where models optimize for superficial aspects of the reward, such as stylistic elements, rather than the underlying knowledge or capability. This is a crucial oversight, as it limits the paper's ability to draw meaningful conclusions about the generalizability of its findings to real-world LLM alignment challenges. The current framing of the problem, while interesting, lacks a strong connection to the broader literature on reward hacking and its implications for model safety and reliability. The paper should also consider the potential for adversarial examples that could further expose the vulnerabilities of the strong model in the weak-to-strong generalization paradigm.

### Questions
Can you clarify is reward hacking along a particular dimension of knowledge is what this paper considers. In other words, in the typical reward hacking behaviors seen during aligning LLMs, the dimension could be style and knowledge. Whereas here we would like to understand tradeoff of two different areas of knowledge, where the strong model reward hacks one knowledge area extensively, at the cost of the other area? If this understanding is correct, it makes the paper much more stronger by making these strong connections.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paradigm of weak-to-strong generalization constitutes the training of a strong AI model on labels given by a weak AI model, and the operating observation is that such a weakly-supervised strong model still outperforms its weak supervisor on the ground-truth data. This paper studies when this procedure could go rogue. Namely, the strong model may indeed result in overall better test accuracy than the weak model, but it may be malicously mislabelling certain data points that are beyond the scope of the weak model to decipher. The authors term this notion as weak-to-strong deception, and propose a metric beyond test accuracy (which they term the "decpetion score") to measure it.

Such weak-to-strong deception may specifically arise when the strong model is trained to minimize conflicting alignment objectives like helpfulness vs harmfulness. The authors state that sacrifice in performance/mislabelings (termed "conflict tax") when the weakly supervised strong model is trained to optimize conflicting objectives ought to occur in the following regions of the data domain in decreasing order: strong-unknown-weak-unknown, strong-unknown-weak-known, strong-known-weak-known, strong-known-weak-unknown. When a significant conflict tax gets paid in the last of these regions, that is when weak-to-strong deception takes place. The authors thus propose a metric to measure this, which they term as the Deception Score (DS), which is simply the fraction of the test data that the weakly-supervised strong model labels differently as compared to a strong model trained on ground-truth data, that belongs to the strong-known-weak-unknown region. (Refer to Equations 2, 8).


The primary experimental settings that the authors consider are those of reward modelling and preference alignment. The authors artifically insert conflicting objectives into the objective function of the weak supervision (see Equations 4, 5), and measure the deception score for a variety of {weak model, strong model} combinations. The consistent observations are that 1) deception scores are always positive and that 2) deception scores increase as the gap between strong model and weak model capacity increases. The authors posit that one of the reasons for this is due to the strong-known region increasing as the strong model becomes larger. The qualitative conclusion from the experiments on the preference alignment task are also the same.

Finally, the authors study how the weak-to-strong deception issue might be fixed. They consider two fixes: 1) supervise the strong model only on a subset of the weakly supervised data that the weak model is most confident on. Unfortunately, the authors find (Figure 10) that this does not greatly improve results. 2) Bootstap, i.e., use the weak supervisor to train a slightly stronger weak model, and supervise the strong model with this latter model. Again, the authors find that this does not largely improve results. These results suggest that fixing weak-to-strong deception will likely require more innovative approaches, and is a complex phenomenon open for future study.

### Strengths
The motivation behind the authors' study is well-founded---weak-to-strong generalization (WTSG) is going to be the predominant paradigm governing alignment of increasingly strong AI models, and studies on possible security issues in the WTSG pipeline are going to be crucial going forward. The authors propose a natural measure to study when the strong model might "fool" the weak model into believing that it is doing better and has achieved WTSG. In particular, improved test accuracy is not really all of the story, and measures like Deception Score (which I found to be an interesting and natural quantity) that the authors propose are also going to be crucial to control. The empirical results in the paper are consistent and insightful, suggesting that weak-to-strong deception as measured by the deception score is a pertinent issue in the WTSG pipeline. The paper opens up interesting and relevant future directions of study to further control such deception phenomena.

### Weaknesses
I feel that the paper could use some more motivation and discussion about the particular form of the objective functions that the authors propose for modeling "conflicting objectives" (namely Equations 4 and 5). How do these objectives model the "helpfulness vs harmfulness" example that the authors mention in the introduction? The authors simply state these objective functions, and they do not really discuss how they are a natural way to model conflicts. The authors should also elaborate a little more on the way they measure the region $S_k \cap W_{uk}$ on line 310. There is a subtlety here that in that $\theta_s^{gt}$ is being used instead of $\tilde{\theta}_s^w$, and I believe this merits a couple lines of discussion.

### Questions
1) I am curious about what the Deception Scores are when there is no conflict in the objective? Namely, what would Figures 5 and 6 look like for the No Conflict objective??

2) Is there any meaningful interpretation of the Deception Score for standard classification/regression tasks (as opposed to reward modeling/preference alignment considered in the paper)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors identify a novel phenomenon known as weak to strong deception that can occur when a weaker model acts as a teacher for a stronger student model. They define weak to strong deception as the stronger student model producing unwanted responses on examples the weak model is un-confident in. This poses a potential future security issue as humans try to align models that are more capable than themselves.

To demonstrate the ubiquity of the weak to strong deception phenomenon, the authors use a variety of weak models to train stronger models in reward modeling and preference alignment settings.

### Strengths
The authors present empirical demonstrations of weak to strong deception in a healthy variety of weak teachers and strong student models. The finding that weak to strong deception correlates with model capability has important implications for the alignment of superhuman models.

### Weaknesses
Generally, I believe the presentation of the core ideas is not particularly clear. In particular, I had a hard time parsing the motivation for the competing optimization objectives that the authors use to define weak to strong deception. This is important because as I understand it, the authors measure deception by analyzing the samples on which the weakly trained model is correct if no competing optimization goal is present and incorrect if the competing optimization goal is present. Along these lines I have some specific questions/concerns.

(i) In my mind weak to strong deception is a more general phenomenon: If we train a strong model with a weak teacher, the "penalty" (compared to training on gold standard labels) should be primarily felt on areas where the weak teacher is unsure. I don't see why this can only be studied as an effect of competing optimization objectives. In particular, a reasonable "baseline" for me seems to be to compare the student model trained on weak labels and trained on gold standard labels and to examine the number of new errors in $S_k \cap W_{uk}$. Is there something I am missing? In other words, could the authors please clarify why they chose to study weak to strong deception as a phenomenon induced by competing optimization objectives?

(ii) Related, the explicit conflict optimization objective seems rather artificial. As I see it, this is essentially just injecting adversarial samples into the loss, so it seems rather unsurprising that this would lead to some mistakes in $S_k \cap W_{uk}$. I guess I would expect this to hold even if ground-truth data were used. Furthermore, the primary results presented in the weak-to-strong preference alignment setting are under this explicit conflict regime. 

(iii) I found figure 7 enlightening. Is there a reason why the authors do not present such a figure for the implicit conflict regime?

In general, I think that the paper would improve if more comparisons to models trained on gold standard labels (and even base models provided no training) were provided. In particular, in the explicit conflict regime, how does the weak to strong deception score change if the model is trained on gold standard labels or not given any training? I think such a study will help isolate the effect of weak training from the effect of the choice for competing optimization objective.

**Minor suggestions**
I think the notation $f(x|\theta_m^d)$ could be misleading. For example, $f(|\theta_s)$ and $f(|\theta_w)$ are *not* different parameters in the same model class, rather they are entirely different models (eg gpt2 vs gpt2-XL). Probably, $w$ vs $s$ should be indexed over the $f$?

There are some concurrent works the authors could consider including.

[1] Yang etal. Weak to strong reasoning. 2024.
[2] Somerstep et al. A statistical framework for weak to strong generalization. 2024
[3]  Wu and Sahai. Provable Weak-to-Strong Generalization via Benign Overfitting. 2024

### Questions
See above

### Soundness
3

### Presentation
2

### Contribution
2
