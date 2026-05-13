# EditRoom: LLM-parameterized Graph Diffusion for Composable 3D Room Layout Editing

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Given the steep learning curve of professional 3D software and the time-consuming process of managing large 3D assets, language-guided 3D scene editing has significant potential in fields such as virtual reality, augmented reality, and gaming. However, recent approaches to language-guided 3D scene editing either require manual interventions or focus only on appearance modifications without supporting comprehensive scene layout changes. In response, we propose \textbf{\modelname}, a unified framework capable of executing a variety of layout edits through natural language commands, without requiring manual intervention. Specifically, \modelname leverages Large Language Models (LLMs) for command planning and generates target scenes using a diffusion-based method, enabling six types of edits: \texttt{rotate}, \texttt{translate}, \texttt{scale}, \texttt{replace}, \texttt{add}, and \texttt{remove}. To address the lack of data for language-guided 3D scene editing, we have developed an automatic pipeline to augment existing 3D scene synthesis datasets and introduced \textbf{\modelname-DB}, a large-scale dataset with 83k editing pairs, for training and evaluation. Our experiments demonstrate that our approach consistently outperforms other baselines across all metrics, indicating higher accuracy and coherence in language-guided scene layout editing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Given a source 3D scene and a natural language command describing the scene edits, the paper presents a method to generate the  corresponding 3D edited scene.

The existing gaps that motivate this paper are three folds: (a) Requiring manual intervention to perform 3D scene edits, (b) limited number of edits and a lack of support for multi-operational textual commands, and (c) lack of a language-guided scene editing dataset, making it difficult to train and evaluate scene-editing models.

To this end, the contributions of the paper include proposing a new approach that combines an LLM (to encode edit commands) with a graph diffusion model (to incorporate scene edits from the input language command) to effectively serve the high-level goal of synthesizing a 3D scene based on natural-language edits/commands. The framework is termed “EditRoom”. In addition to the proposed approach, the paper also introduces a new synthetic scene editing dataset named “EditRoom-DB” with 83K pairs of language+edited 3D scene, spanning 16K initial 3D scenes.

To summarize, EditRoom takes as input a source scene and a natural language command describing scene edits, and outputs a corresponding edited scene. The dataset used is “EditRoom-DB”, which is a new dataset of scene editing pairs created from 3D-FRONT  dataset. GPT-4o is the LLM used, and there is a graph-transformer based diffusion model. The learning setup is strongly supervised. The loss functions involved are KL divergence loss and diffusion loss for graph diffusion model and layout diffusion model. In terms of evaluations, the paper looks at the following four quantitative metrics: (1) IoU score: 3D IoU between objects in pre-edit and post-edit scene, and selecting pairs with highest 3D IoU value (Q: how many pairs do you use?) (2) S-IoU score: semantic similarity between captions of matching objects as measured by Sentence BERT (Q: how do you find caption for generated objects?) (3) LPIPS: determines pixel similarity between 24 views of pre-edit and post-edit scenes, and (4) CLIP score: Using CLIP-ViT-B32 to find semantic similarity between 24 views. As for comparisons, the paper compares against two works: DiffuScene-N (modified version of existing 3D scene synthesis model DiffuScene, from CVPR 2024), and  ScenEditor-N. (Spelling mistake: Line 323, the name of the baseline should be DiffuScene-N, instead of DiffuScene-E)

### Strengths
1) Well-written paper
2) The idea of breaking down command into multiple steps is interesting
3) The proposed model can be used for multi-operation editing without explicitly training
on such commands. This is a useful feature for interior designers
4) The newly introduces dataset “EditRoom-DB” is quite useful to the 3D scene research community

### Weaknesses
1) The motivation to use diffusion model is unclear.
2) Out of the two compared methods, only one, DiffuScene-N, is based on an existing work (viz., DiffuScene, from CVPR 2024, Tang et. al.). The other one is a modified version of the proposed approach. This is good, But, why not use a modified version of InstructScene (Haque et. al., ICLR 2024) and also of EchoScene (Zhai et.al. , ECCV 2024) as well? This would be tell a good story on how effective the proposed approach is. This is a weakness, something I believe can be addressed.

### Questions
1) Is the scene edit one-shot (i.e., take all edit commands at once and generate a scene) or progressive (i.e., edit the 3D scene one command at a time)?
2) Motivation behind using a diffusion model is unclear. If the edits allowed are simply adding,
removing, replacing, scaling, translating and rotating an object (even the relations
between objects are pre-defined and limited), why do you need to train a diffusion
model? You could perform these tasks directly on the source scene graph by
adding/removing/replacing a node and then retrieving an object from the given object
database that fits the text description (see Language-Driven Editing of 3D Scenes from Scene Databases, SIGGRAPH 2018; missing this reference). Using diffusion model makes sense when one
wants to generate an entirely new scene/new object from scratch. In the scene editing
task, we are given with an initial scene and our task is to modify it.
3) How does the diffusion process look like for, say, rotation operation? It would be
helpful to have visualizations of intermediate diffusion steps. Applying rotation to
existing object can be done analytically. Why would we need a diffusion model? I would consider this a weakness of the paper as it precludes some important visualizations pertaining to the proposed approach and something that is relevant to the end results. 
4) Regarding the proposed dataset “EditRoom-DB”, what is the reason behind having only
500 examples as test data? This number is too small compared to the number of
training samples i.e. 83k. The standard practice is to have a certain percentage (say,
10%) of total samples as test data. Looking at Table-1, dataset in its current form is
biased towards “bedroom” category because it has ~50k training and only 500 test
samples, as compared to ~18k train and 500 test samples for “dining room” category.
The ratio of train-test data is high for bedroom scenes compared to the other two categories, and its
effect is seen in the results Table-2 (high performance for bedroom than dining and
living room). It would be a good experiment to run when you keep the train:test ratio
equal for all categories and see if the model gives comparable results.

Overall, the paper proposes a novel 3D indoor scene editing model that uses LLM to encode
scene editing instruction and a graph-diffusion model to perform scene edits. Moreover, it introduces a 
new dataset for training and evaluating 3D indoor scene editing task.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces EditRoom, a two-module scene editing framework based on natural language prompts. First, the command parameterizer converts natural language prompts into sequences of breakdown commands for six editing types using an LLM. Then, the scene editor constructs the target scene from the source one using the proposed conditional graph generation models based on diffusion. Quantitative and qualitative results prove the effectiveness and generalization capability of the proposed approach.

### Strengths
a) The problem studied in the paper is important for real-world applications. b) This paper introduces a synthetic scene editing dataset called EditRoom-DB, contributing to the field. c) Support for multi-operation commands enhances the practicality of the proposed approach.

### Weaknesses
 a) Comparison with baselines: The authors mention the difficulty of adapting scene synthesis methods for layout editing, and thus compare with only two baselines. However, several LLM-based methods using in-context learning (e.g. LayoutGPT) could potentially be adapted to support editing by defining the task for the LLM and conditioning on in-context learning samples from EditRoom-DB. Including such a comparison with in-context learning-based methods would enhance the evaluation.  Specifically, the comparison should include a more rigorous approach to in-context learning, such as selecting in-context examples based on the specific edit type being performed, rather than random selection. This would provide a more controlled and fair comparison. b) Missing complexity analysis: In this work, the authors train two graph diffusion models, however the complexity analysis is missing. How much time do the training and inference take?

### Questions
All of my questions are listed in the weaknesses section, and I may adjust the rating if they are well addressed.

### Soundness
3

### Presentation
4

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
This paper proposes EditRoom for 3D layout editing of an existing room. It first uses GPT-4o to parse the natural language instruction into a sequence of breakdown commands, and then trains a diffusion model to generate the edited layout based on the commands. The framework is reasonable and utilize the state-of-the-art LLM and generative diffusion model. The proposed approach generates good results and outputs the other variants of itself, validating the effectiveness of using GPT-4o to infer the breakdown commands and the design of the graph diffusion model as 3D scene editor.

### Strengths
The strengths include:

1. It proposes the 3D layout editing pipeline, which uses GPT-4o as the command parameterizer and a graph diffusion model as the scene editor.

2. The graph diffusion is tailored to deal with the layout editing problem and outperforms the adapted DiffuScene approach.

3. It constructs a large dataset composed of the paired scene layouts and the corresponding editing instructions, which facilitates the following language-based 3D layout editing research.

### Weaknesses
 **Firstly, it lacks the discussion of the motivation for the target problem: why and when a user would prefer a language-based 3D layout editing rather than interactively modify the one or two object placements by himself?** This relates with the design of evaluation experiments. Intuitively, the problem setting should be a complicated editing and a very rough instruction. For example, the user might not explicitly specify all the atom editing, but rather describe the key intent only. Or it requires a series of operations to make enough space to enable the target editing. The single-operation and multi-operation cases shown in the paper seem straightforward. Actually, the second row  in Fig.4 gave a good example, since a user might express “rotate the bed” but desire to have the bed s well as the accompanied nightstand rotated together. But it seems that the proposed approach only edit the objects that are explicitly specified, and produces an unreliable layout result.

**Secondly, it lacks the comparison with heuristic methods.** The proposed approach trains a graph diffusion model as the scene editor. But the paper only compare with DiffuScene (another diffusion model for 3D room layouts) and its own variants, only to validate the key designs such as taking breakdown commands as conditions and the condition types of the network. In fact, training neural networks for 3D layout problem often aims to deal with high-level conditions and efficiently generate plausible layouts. Given that the GPT-4o has already inferred the breakdown commands and the generative process of diffusion model is slow, do we really need such a network to produce the edited layout? What if directly parse the breakdown commands to modify the specified object? What if using a simulated annealing algorithm as a post-processing step to deal with the possible collisions? At least it alleviates the demand for constructing a training dataset.

**Thirdly, it lacks a detailed discussion of the command parameterizer.** Currently, there are different opinions on whether the LLM has satisfactory spatial reasoning ability. Fig.5 is a good example as the goal is to make the two nightstands symmetric with each other. But it seems the LLM response presented in the figure is incomplete. It is important to give a in-depth and detailed analysis on the LLM performance, e.g. when the LLM would fail and how to promote its ability?

There are some minor issues. For example, are the point cloud of each object (line 227) only point locations or rgb color as well? How to “concatenate each element of source scene graphs into noisy target scene graphs” (line 241)? It means to concatenate the attributes of corresponding elements, or merge the node lists?

### Questions
Overall, this paper presents a novel framework for language-based 3D room layout editing. The main weaknesses lie in the motivation and evaluation of the proposed approach. The current evaluation only validate the key designs under the novel framework (first LLM and then a diffusion model), but lacks the explanation on why this framework is essential (especially the diffusion model as a scene editor).

### Soundness
2

### Presentation
3

### Contribution
2
