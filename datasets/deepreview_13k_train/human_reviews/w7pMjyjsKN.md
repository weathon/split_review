# Counterfactual Concept Bottleneck Models

- Decision: Accept
- Scores: 5, 6, 8, 8

## Abstract
Current deep learning models are not designed to simultaneously address three fundamental questions: \textit{predict} class labels to solve a given classification task (the "What?"), \textit{simulate} changes in the situation to evaluate how this impacts class predictions (the "How?"), and \textit{imagine} how the scenario should change to result in different class predictions (the "Why not?"). The inability to answer these questions represents a crucial gap in deploying reliable AI agents, calibrating human trust, and improving human-machine interaction. To bridge this gap, we introduce CounterFactual Concept Bottleneck Models (CF-CBMs), a class of models designed to efficiently address the above queries all at once without the need to run post-hoc searches. Our experimental results demonstrate that CF-CBMs: achieve classification accuracy comparable to black-box models and existing CBMs (“What?”), rely on fewer important concepts leading to simpler explanations (“How?”), and produce interpretable, concept-based counterfactuals (“Why not?”). Additionally, we show that training the counterfactual generator jointly with the CBM leads to two key improvements: (i) it alters the model's decision-making process, making the model rely on fewer important concepts (leading to simpler explanations), and (ii) it significantly increases the causal effect of concept interventions on class predictions, making the model more responsive to these changes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors extend the concept bottleneck model framework to allow simulation of counterfactual concepts and labels. The method is based on a variational approach that models concepts as latent confounders, and approximates this posterior using concept labels at training time. This extension opens the door to explaining prediction at a finer level of detail, focusing on intermediate concepts rather than pixel values.

### Strengths
The authors tackle an extremely challenging problem (counterfactual reasoning using deep learning); making meaningful progress along this direction would have a big impact.

The authors show how training using a structured objective allows for test-time manipulations that shed light on how predictions are made

They extend CBM to include counterfactual sampling, which in principle allows a single model to estimate quantities at all three levels of Pearl’s ladder of causation.

The proposed method relies on concept labels, which may be difficult to collect in realistic settings.

### Weaknesses
The authors tackle an extremely challenging problem (counterfactual reasoning using deep learning); making meaningful progress along this direction would have a big impact.

The authors show how training using a structured objective allows for test-time manipulations that shed light on how predictions are made

They extend CBM to include counterfactual sampling, which in principle allows a single model to estimate quantities at all three levels of Pearl’s ladder of causation.

The proposed method relies on concept labels, which may be difficult to collect in realistic settings.

The training objective is fairly complex and introduces many hyperparameters. The authors do not discuss how to tune these.

There is a disconnect between the working example of x-ray imaging and the types of datasets considered in the experiments.

I felt that details of the SCM design and subsequent training (e.g. ignoring p(x|z)) were not justified

Additional comments/questions: 
* [L042-044] This is a bold claim....what about the field of XAI? Pearl's ladder of causality has been quite influential in deep learning (including XAI), so I would assume that any methods aimed at counterfactual explanations would address these questions to some extent.
* I find the abstract a bit strange. Causal inference is a broad field attempting to answer (from a statistical perspective) the how and why questions, but it is not explicitly mentioned. Also, "existing CBMs" are mentioned in passing but the authors don’t say what they are or how they work. Maybe it would be better to more precisely situate the paper in the context of recent attempts to integrate causal inference with deep learning.  
* [Sec 2] I don't insist, but it would be nice to see a citation acknowledging early efforts of using VAEs for causal inference [https://proceedings.neurips.cc/paper/2017/hash/94b5bde6de888ddf9cde6748ad2523d1-Abstract.html]
* [Eqn 1, L123] I don't understand why sampling a counterfactual concept c' does not also require sampling a fresh set of covariates x'. It seems to me that for concepts that matter in the real world, you would need to update the observed features as the concept is manipulated. To ground this in the x-ray example, if the concept is changed from "narrow joint space" to "bone spurs", would the distribution over pixels not also need to be updated? Clarifying this point seems important to justify why the $p(x|z)$ term is ignored in the optimization [L152].
* [L169] how are specific values for $\lambda_i$ [Table 6] chosen? Was a validation set used for tuning? Is the method sensitive to these values? I'm not satisfied with "these details are in the released code" [L850]
* [L260-265] The experiments inherit some datasets from prior papers, such as Koh et al 2020. Is there a reason why the OAI x-ray dataset from that paper was not used? X-rays are used as a working example throughout the paper [Fig 1, Fig 2, Sec 3.2] so this omission surprised me.
* [Sec 4, Sec 5] How does the method do when asked to simulate concept pairings that are OOD w.r.t. its training data? I would imagine for the CUB dataset there will be combinations of bird characteristics that are not represented by real-life birds; is it possible to examine the predictions for these concepts?. The strength of human counterfactual reasoning comes in part from OOD generalization, e.g. imagining a pink elephant. Replicating this using ML seems quite difficult. In the end I still have questions around whether what is being done here is meaningfully different from structured generative/discriminative modeling [L503-509] with interpretable features that can be adjusted on the fly. I think this is certainly related to counterfactual reasoning, but may not encompass it completely.
* [L516] If I express the counterfactual as E[Y|do(X)=X', Y=Y'] and the interventional as E[Y|do(X)=X'], then it would seem that counterfactual explainability methods can answer the "how" question by just marginalizing out the specific observation, i.e. E[Y|do(X)=X'] = E_{Y'}[ E[Y|do(X)=X', Y=Y']. You could replace the observation being a label (Y=Y') with the observation being a concept or other covariate as needed. Is there something wrong with this line of reasoning? Modeling counterfactuals seems more challenging than modeling interventions, so I am wondering if the authors have thought of how to go from one to the other in a post-hoc manner without designing a method that explicitly models all three levels of Pearls' ladder.

### Questions
Additional comments/questions: 
* [L042-044] This is a bold claim....what about the field of XAI? Pearl's ladder of causality has been quite influential in deep learning (including XAI), so I would assume that any methods aimed at counterfactual explanations would address these questions to some extent.
* I find the abstract a bit strange. Causal inference is a broad field attempting to answer (from a statistical perspective) the how and why questions, but it is not explicitly mentioned. Also, "existing CBMs" are mentioned in passing but the authors don’t say what they are or how they work. Maybe it would be better to more precisely situate the paper in the context of recent attempts to integrate causal inference with deep learning.  
* [Sec 2] I don't insist, but it would be nice to see a citation acknowledging early efforts of using VAEs for causal inference [https://proceedings.neurips.cc/paper/2017/hash/94b5bde6de888ddf9cde6748ad2523d1-Abstract.html]
* [Eqn 1, L123] I don't understand why sampling a counterfactual concept c' does not also require sampling a fresh set of covariates x'. It seems to me that for concepts that matter in the real world, you would need to update the observed features as the concept is manipulated. To ground this in the x-ray example, if the concept is changed from "narrow joint space" to "bone spurs", would the distribution over pixels not also need to be updated? Clarifying this point seems important to justify why the $p(x|z)$ term is ignored in the optimization [L152].
* [L169] how are specific values for $\lambda_i$ [Table 6] chosen? Was a validation set used for tuning? Is the method sensitive to these values? I'm not satisfied with "these details are in the released code" [L850]
* [L260-265] The experiments inherit some datasets from prior papers, such as Koh et al 2020. Is there a reason why the OAI x-ray dataset from that paper was not used? X-rays are used as a working example throughout the paper [Fig 1, Fig 2, Sec 3.2] so this omission surprised me.
* [Sec 4, Sec 5] How does the method do when asked to simulate concept pairings that are OOD w.r.t. its training data? I would imagine for the CUB dataset there will be combinations of bird characteristics that are not represented by real-life birds; is it possible to examine the predictions for these concepts?. The strength of human counterfactual reasoning comes in part from OOD generalization, e.g. imagining a pink elephant. Replicating this using ML seems quite difficult. In the end I still have questions around whether what is being done here is meaningfully different from structured generative/discriminative modeling [L503-509] with interpretable features that can be adjusted on the fly. I think this is certainly related to counterfactual reasoning, but may not encompass it completely.
* [L516] If I express the counterfactual as E[Y|do(X)=X', Y=Y'] and the interventional as E[Y|do(X)=X'], then it would seem that counterfactual explainability methods can answer the "how" question by just marginalizing out the specific observation, i.e. E[Y|do(X)=X'] = E_{Y'}[ E[Y|do(X)=X', Y=Y']. You could replace the observation being a label (Y=Y') with the observation being a concept or other covariate as needed. Is there something wrong with this line of reasoning? Modeling counterfactuals seems more challenging than modeling interventions, so I am wondering if the authors have thought of how to go from one to the other in a post-hoc manner without designing a method that explicitly models all three levels of Pearls' ladder.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a method that combines counterfactual and concept bottleneck that can answer "What?", "How?" and "Why not?" all at once. It leverages latent variable models to generate counterfactuals via variational inference. It achieves comparable classification accuracy to standard CBMs and black-box models and outperforms in generating interpretable, concept-base counterfactuals.

### Strengths
1. The method is straightforward and intuitive, combining two existing approaches, counterfactual reasoning and concept bottleneck modeling with moderate novelty. The experiments provide solid evidence of its effectiveness.
2. This paper is well organized, and abstract and introduction effectively set the stage for the paper's major content.
3. The method enhances the interpretability of counterfactuals, making it potentially valuable for many real-life settings like medical applications, as the authors suggest, beneficial for clinical decision-making processes.

### Weaknesses
1. While the paper uses 3 datasets, they are relatively simple. In this paper, authors use examples of medical images (fig 1) but did not actually experiment with any medical dataset. Using more diverse and complex real-life dataset (e.g., CIFAR-100 or MIMIC-CXR) would strengthen the paper and demonstrate broader applicability. The current datasets, while suitable for initial validation, do not fully capture the complexities inherent in real-world applications, particularly in the medical domain where nuanced features and high dimensionality are common. The lack of experiments on medical datasets, despite using medical images as a motivating example, is a significant gap.
2. The paper lacks visualizations of counterfactuals. For example, when discussing improvements in counterfactual quality, it would be helpful to show visual comparisons with baselines. Providing real counterfactual comparisons would better substantiate the claims and help readers understand the model's advantages. Specifically, the absence of visual examples makes it difficult to assess the practical impact of the proposed method on interpretability. While the authors claim enhanced interpretability, this is not directly demonstrated through visual means, which are crucial for understanding counterfactual changes in complex data.

### Questions
Could you provide additional visual examples of counterfactuals generated by your model and baseline methods for each dataset? Visualizing these comparisons would be highly intuitive and beneficial for readers, helping them clearly see the improvements.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a concept bottleneck model with the ability to generate counterfactual explanations. The paper aims to answer three questions: what, how and why not. The what questions are answered by showing the concepts used to make predictions. The how questions are answered by changing the concepts and observing how the prediction changes. Finally, why not questions can be answered by providing an alternative outcome and observing how the concepts change to understand what-if situations. The method also enables what the authors call “task-driven” interventions that allow users to correct wrongly predicted concepts. The models are tested on three datasets: dSprites, MNIST add CUB, and tested on various metrics. In general, based on the experiments, the proposed model demonstrates good performance across multiple tasks and datasets.

### Strengths
- The paper is easy to read, and the figures are well described and informative.
- Explanations seem to be easy to use.
- The method is tested against many baselines.

### Weaknesses
 - I am concerned regarding the number of hyperparameters that need to be set for the loss function. It is not clear how important they are, and how much tuning is needed. How easy is it to tune these hyperparameters? How do they affect the results? Is it easier to have separate systems rather than one big as the one proposed?
- The method requires handcrafted concepts, and it might not be easy to come up with these concepts. Further, there might be a lot of labor involved in creating these concepts. Moreover, the predictive performance depends on how well these concepts describe the input features.
- Figure 1: Is it only for illustration or is this actually the result from trained models on x-ray images?
- I might have missed it, but I cannot find the citation for the dataset from which the x-ray images come. If I did not miss it, please cite it so it becomes easier for readers to find it. Moreover, are there any restrictions on showing these images, that is, what is the license of these images?
- I believe the x-ray images to be from the Osteoarthritis Initiative dataset. It is used to motivate the paper, but why is it not used in the experiments? Are there any weaknesses with the method making the dataset unsuitable for experimentation and showcasing results?
- Line 156: Why does z' need to be conditioned on both c and y? Don't we already know y if we know c?
- Line 224: How do we know Equation 5 gives us sparser explanations? Is it because the posterior is moved towards the prior distribution? But this is defined in the latent space. How can we know that the concepts c will be sparse even though the posterior of z is close to the prior?
- How are the models trained? Are certain parts frozen, or are all components trained jointly?
- Is it possible to show readers the explanations themselves for the datasets used and not only Figure 1 for a dataset not used? We have seen many quantitative results, but part of XAI also involves qualitative qualities. How do these explanations perform qualitatively with end-users? Are they useful to human end-users? And who are the intended end-users for these explanations?
- Although we do not need to run post-hoc searches, new black-box components are introduced into the model. How does that affect the overall interpretability of the model? I believe that can also have negative side effects and not only positive influences.

### Questions
- Please refer to the weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces the framework of counter factual CBMs, aimed specifically to increase the variability and depth of inspection question that can be asked towards a CBM. In other words, CF-CBM aims to increase the level of interpretability and interactability of standard CBM models without losing performance.

### Strengths
The paper is very well written and structured. It is well motivated and the methodological contribution as far as I can tell is clear and important.

### Weaknesses
I just have a few minor remarks which I have added to the questions section.

- 5.1 I find it important to have the results of this question also in the main paper, e.g., average values, as it is an important one. I would additionally suggest the authors change the wording of the conclusion. It seems that on average CF-CBMs are slightly lowerd in predictive performance. While I don’t think this is a drawback of the proposed emthod, I think stating the method is on par is slightly overstated. That CF-CVM is not necessarily on par is an important information for the reader/user. Again stating this won’t decrease the contribution. 

- 5.2. I don’t understand the intuition behind why CF-CBMs should be less prone to confounding factors? What mechanism in their learning is beneficial for this? Maybe an ablation study would be intersting to underscore these findings.

- Please provide code to the paper, e.g., an anonymized github link.

- Lastly, this [1] might be an interesting paper to add to the Introduction as it tackles learning concepts (e.g., for CBMs) focussing on learning inspectable concepts, e.g., via counterfactual querying. Of course [1] focuses on counterfactual concepts, whereas this work focuses on counterfactuals for a model decision.

### Questions
- 5.1 I find it important to have the results of this question also in the main paper, e.g., average values, as it is an important one. I would additionally suggest the authors change the wording of the conclusion. It seems that on average CF-CBMs are slightly lowerd in predictive performance. While I don’t think this is a drawback of the proposed emthod, I think stating the method is on par is slightly overstated. That CF-CVM is not necessarily on par is an important information for the reader/user. Again stating this won’t decrease the contribution. 

- 5.2. I don’t understand the intuition behind why CF-CBMs should be less prone to confounding factors? What mechanism in their learning is beneficial for this? Maybe an ablation study would be intersting to underscore these findings.

- Please provide code to the paper, e.g., an anonymized github link.

- Lastly, this [1] might be an interesting paper to add to the Introduction as it tackles learning concepts (e.g., for CBMs) focussing on learning inspectable concepts, e.g., via counterfactual querying. Of course [1] focuses on counterfactual concepts, whereas this work focuses on counterfactuals for a model decision.

[1] Wolfgang Stammer, Antonia Wüst, David Steinmann, and Kristian Kersting. “Neural Concept Binder.” In: Advances in Neural Information Processing Systems (NeurIPS) (2024)

### Soundness
3

### Presentation
3

### Contribution
3
