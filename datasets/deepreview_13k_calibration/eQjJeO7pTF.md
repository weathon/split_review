# Generative Location Modeling for Spatially Aware Object Insertion

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3, 5

## Abstract
Generative models have become a powerful tool for image editing tasks, including object insertion.
However, these methods often lack spatial awareness, generating objects with unrealistic locations and scales, or unintentionally altering the scene background.
A key challenge lies in maintaining visual coherence, which requires both a geometrically suitable object location and a high-quality image edit.
In this paper, we focus on the former, creating a \emph{location model} dedicated to identifying realistic object locations.
Specifically, we train an autoregressive model that generates bounding box coordinates, conditioned on the background image and the desired object class.
This formulation allows to effectively handle sparse placement annotations and to incorporate implausible locations into a preference dataset by performing direct preference optimization. 
Our extensive experiments demonstrate that our generative location model, when paired with an inpainting method, substantially outperforms state-of-the-art instruction-tuned models and location modeling baselines in object insertion tasks, delivering accurate and visually coherent results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper focuses on proposing a location model to identify realistic object location in an image. This model is then further combined with the inpainting module is used to outperform SOTA instruction tuned models and location modeling baselines.

### Strengths
1. The paper is decently written paper, but it can still improve it's clarity. 
2. The proposed experiments and the use of potive and negative locations in conditioning the model seems interesting.

### Weaknesses
1. First and foremost the paper specifies a model for localisation using an autoregressive model. One simple question, can the model use a mask using a model like segment anything model (SAM) to localise the object and simply use the inpainting model.
2. Second make the equations and it's more clear, such as equation 3, the reviewer is assuming it to be the "order".  
3. The alternative inpainting models such as SmartBrush, LeftRefill etc, are not well explored.

### Questions
Please refer to the questions on the weakness and try to address those.

### Soundness
2

### Presentation
2

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
This paper presents a novel approach to object insertion in images, focusing on the generation of realistic object locations, which, when paired with an inpainting method, leads to visually coherent and accurate results.  This paper trains an autoregressive model that generates bounding box coordinates, conditioned on the background image and the desired object class, allowing to effectively handle sparse placement annotations and to incorporate implausible locations into a preference dataset by performing direct preference optimization.  Experiments show that this approach achieves better performance in location modeling and significantly outperforms instruction-tuned image editing models in object insertion tasks.

### Strengths
The paper presents a novel two-step process for object insertion, focusing on location modeling to improve the realism of object placement. Demonstrated superior performance in object insertion tasks, particularly in maintaining visual coherence.

### Weaknesses
Computational Cost: The addition of a location model might increase the overall computational burden of the system.
Data Dependency: While the model can work with sparse annotations, I think its performance remains heavily dependent on the quality of the dataset.

### Questions
Overall, I think the paper technically makes sense, but some questions need further discussion or resolution.

Q1: The paper pursues the accuracy of reasonable insertion target positioning, but for artistic creation, imagination needs to be infused. I am curious about the effect of inserting and editing imaginative objects. For example, what if the inserted object is a car with wings? Would the car be placed on the ground or in the air? Or could you provide other examples?

Q2: Can the method handle multiple targets? I am interested in whether the detection model has its own preferences. For instance, if the prompt is "add an apple to the top left and top right corners," how does the method in this paper deal with such a scenario?

Q3: I am not entirely sure about the motivation behind the application. Since the method in this paper first generates candidate positions and then performs inpainting to improve the reasonableness of the generated target, if the target position is so crucial, why not opt for manually drawing a candidate box on the background and then editing? This step is not complicated, and the position of the box should better align with the user's needs. My understanding is that this paper achieves automatic target box generation, but it adds a new model for generating boxes that comes with additional costs in terms of time, memory, and GPU resources. So, what extra advantages does this approach offer over manual box drawing?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents the novel task of generative location prediction for object insertion in images. Given an input backgorung image and an object categories, the proposed method predicts plausible locations for placing an object of the queried category in the backgorund image. 

Specifically, authors propose training a conditional auto-regressive generative model, which predicts a spatial probablility distribution for the boundig boxes where the object can be placed. The proposed model is trained in two stages: first, the model is trained on two datasets using positive annotations of plausible locations for the objects. Then, a small dataset contatining both positive and negative annotations is used to further optimize the model using a preference optimizaiton technique. 

The authors evaluate their proposed method in two setups: 
1. locatoin modeling, where the model and its baselines are evaluated in their ability to predict plausible object locations,
2. Object insertion, where the model is compared to the baselines in their impact on image editing methods when used to create an object in an image.

### Strengths
- Location prediction for object insertion is a novel and challenging task, which has not been addressed in previous studies. The addressed task has multiple useful applications, and this work opens the door for furhter explorations of this problem.

 - The use of preference alignment in addition to the standard training of the autoregressive model is effective in improving the performance by exploiting available negative samples.

- Based on the provided evaluations, the proposed method is effective in providing reasonable locations for object inpainting methods compared to implicit location modeling done in currect editing models.

### Weaknesses
 - The proposed approach heavily relies on annotated training datasets. Acquiring large dataset with rich annotations for such method is very difficult, considering many possibilities for annotations per image. My main concern is how well the proposed method generalizes beyond the current training data.

- I could not find any analysis on multiple predictions for the same object category and background image. It would be interesting to see how diverse and plausible are different predictions of the model for the same input.

- The proposed method, while demonstrating improvements over implicit spatial modeling, still exhibits failure cases, particularly in cluttered scenes. The model appears to struggle with complex scenes, sometimes placing objects in implausible locations or overlapping existing objects. Furthermore, the predicted bounding box sizes are not always consistent with the expected object size, indicating a lack of precise spatial understanding.

### Questions
- The proposed method is first trained on PIPE dataset and then on OPA dataset (before preference alignment). Is there a reason the model is not trained jointly on the two datasets?

- As mentioned by the authors, the PIPE dataset could contain inpainting artifacts in many images. First of all, did the authors perform any filtering on such images? and secondly, did the authors analyze if the model tends to take a shortcut for its prediction by using the inpainting artifacts?

- Could the authors confirm if all the provided quantitave results for location modeling evaluation are performed on OPA dataset, where no inpainting is performed on the images?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Generative models have become a powerful tool for image editing tasks, including object insertion. However, these methods often lack spatial awareness, generating objects with unrealistic locations and scales, or unintentionally altering the scene background. A key challenge lies in maintaining visual coherence, which requires both a geometrically suitable object location and a high-quality image edit. In this paper, They focus on the former, creating a location model dedicated to identifying realistic object locations. Specifically, They train an autoregressive model that generates bounding box coordinates, conditioned on the background image and the desired object class. This formulation allows to effectively handle sparse placement annotations and to incorporate implausible locations into a preference dataset by performing direct preference optimization.

### Strengths
They train an autoregressive model that generates bounding box coordinates, conditioned on the background image and the desired object class. This formulation allows to effectively handle sparse placement annotations and to incorporate implausible locations into a preference dataset by performing direct preference optimization.

### Weaknesses
- Novelty. The proposed method finetune the instruction-guided editing dataset and leverage the location model to generate the bbox, It has been appeared in previous mask-free inpainting work. What is the significance and value of using autoregressive models? What is the motivation of this work? I strongly think the motivation is weak.
- Experiment. the lack comparison with  brushnet. 
- The ablation experiment using autoregressive and other models is missing.
- limiting the user's editing freedom.
- Generation with control signal such as depth and other sketch.

### Questions
See  weaknesses

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work presents a two-stage approach for realistic object insertion, enhancing visual coherence by separating "where" and "what" tasks. The model first predicts plausible object positions using an autoregressive transformer, followed by inpainting for object insertion. Direct preference optimization (DPO) refines the location model, leveraging bounding box annotations to improve placement accuracy. Results show it outperforms instruction-based models in addressing unrealistic locations, background distortion, and scaling issues.

### Strengths
- The motivation is clear and the techniques sound reasonable.
- The writing and organization are easy to follow.
- Experimental results indicate that the proposed approach can achieve better performance.

### Weaknesses
1. The proposed approach lacks technical novelty, primarily combining existing location prediction and inpainting techniques. Improving the accuracy of bounding box predictions would naturally enhance the results of 2D/3D inpainting result. 
2. 2D object insertion is a well-explored topic, with numerous works on 2D/3D insertion (including Gaussian Splatting and NeRF) presented at CVPR'24 and ECCV'24. The paper requires some fair and substantial comparison with baselines and other recent inpainting methods to justify its contributions.
3. This work relies heavily on the inpainting model to handle the object’s occlusions and interaction cases. The authors don’t mention how the model performs in highly cluttered or dense environments with multiple potential object placements.

### Questions
- The paper does not show how the model performs in complex environments where multiple potential object placements may exist, which is more promising for the community. 
- I think the authors should do some study on decoupling instructions rather than simply predicting the positions.
- The paper could include more in-depth case studies and analysis, which would provide readers with a clearer understanding of the strengths and limitations of the proposed approach.

### Soundness
2

### Presentation
3

### Contribution
2
