# NextBestPath: Efficient 3D Mapping of Unseen Environments

- Decision: Accept
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
This work addresses the problem of active 3D mapping, where an agent must find an efficient trajectory to exhaustively reconstruct a new scene.
Previous approaches mainly predict the next best view near the agent's location, which is prone to getting stuck in local areas. Additionally, existing indoor datasets are insufficient due to limited geometric complexity and inaccurate ground truth meshes.
To overcome these limitations, we introduce a novel dataset AiMDoom with a map generator for the Doom video game, enabling to better benchmark active 3D mapping in diverse indoor environments.
Moreover, we propose a new method we call next-best-path (NBP), which predicts long-term goals rather than focusing solely on short-sighted views.
The model jointly predicts accumulated surface coverage gains for long-term goals and obstacle maps, allowing it to efficiently plan optimal paths with a unified model.
By leveraging online data collection, data augmentation and curriculum learning, NBP significantly outperforms state-of-the-art methods on both the existing MP3D dataset and our AiMDoom dataset, achieving more efficient mapping in indoor environments of varying complexity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a method to predict paths during mapping that optimize accumulated coverage. The goal is to cover the environment in a minimal time using only a depth sensor.

Point clouds and the robot trajectory are input to an encoder which yields a latent that is decoded into a value map representing the coverage gain and an occupancy map. The cell in the coverage gain map with the highest value is set as the long term goal.

The authors proposed a new dataset AiMDoom played out on a game (simulation) environment, since active methods unlike passive SLAM have to be evaluated on the same environment with different actions/trajectories.

### Strengths
S1: the new dataset has complex challenging lay-outs.

S2:  the new dataset has diversity with a lot of opportunities to evaluate generalization

S3: the decoded occupancy map includes unseen places, behind walls, for example.

### Weaknesses
W1: The main weakness of the paper is the scope of active mapping addressed is only coverage rather than the map itself. While coverage is indeed significant it assumes that  3D reconstructions are error-free (the M in SLAM). Moreover, poses are assumed accurate, an assumption far from reality.

W2: The paper is set in a very narrow context by ignoring the literature on Active SLAM. In particular, active mapping has been based on first principles of information theory. See the excellent exposition here Julio A Placed, Jared Strader, Henry Carrillo, Nikolay Atanasov, Vadim Indelman, Luca Carlone,
and José A Castellanos. A survey on active simultaneous localization and mapping: State of the art and new frontiers. IEEE Transactions on Robotics, 2023

I think the authors would benefit a lot in rethinking their approach and rewriting their paper by reading this article.

W3: The approach is very similar to (Georgakis, 2022). While Georgakis et al. predict occupancy probability and model uncertainty, here the authors predict occupancy and a value map that should have the interpretation of information gain/uncertainty. While Georgakis' objective is point-goal navigation one can use its exploration policy as a pure mapper. Georgakis' value map is based on explicit computation of covariance from ensembles without the use of any ground-truth.
Finally, Georgakis choose long-term goal and then estimate paths based on occupancy maps, similar to the approach here.

W4: The main idea of exploration is trying to choose paths where the measurements are not predictable by the occupancy paths. The expression in (2), however, defines the gain as minimal error to the ground-truth. This will not encourage the agent to go to new unvisited directions but rather to directions where the prediction error will be very small.

W5: There is considerable literature that has been ignored in related work and experimental comparisons. In particular, we would like to see comparisons with 

a.  D. S. Chaplot, D. Gandhi, S. Gupta, A. Gupta, and R. Salakhutdinov, “Learning to explore using active neural SLAM,” in Proc. Int. Conf. Learn. Representations, 2020.

b. A. Bircher, M. Kamel, K. Alexis, H. Oleynikova, and R. Siegwart, “Recedinghorizon“next-best-view”plannerfor3Dexploration,”inProc. IEEE Int. Conf. Robot. Autom., 2016, pp. 1462–1468.

### Questions
Q1. L068: You write "scene uncertainty does not directly align with the ultimate objective of 3D mapping". Is the uncertainty of predicted occupancy not the uncertainty of the 3D map? What do you mean here?

Q2: The computed information gain during training is using the ground-truth ( eq 2) while inference uses the ground-truth instead. It is not clear whether the use of the ground-truth 

Q3: The authors should clarify the first term in eq. 3. What does it mean ground-truth coverage gain?

### Soundness
3

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
4

### Summary
In this paper, the authors focus on improving the reconstruction efficiency of active mapping in a new environment. Previous methods mainly predict the next best viewpoint near the current location and are prone to getting stuck in local areas. 

Instead, the authors propose the leverage accumulated history information to find a long-term goal which could bring the largest gain. At the same time, an obstacle map is predicted to find the long-term goal efficiently. 

In addition to the proposed method, the authors also introduce a new synthetic dataset which has more complicated structures and larger diversities of map than previous datasets. 

Experiments on one public dataset and the new dataset demonstrate that the proposed method outperforms prior methods significantly.

### Strengths
The strengths of this paper are as follows:

1.	A more complicated dataset (AiMDoom) for active mapping. Compared with other either synthetic or real datasets, such as Replica, RoboTHOR, MP3D, and ScanNet, HM3D, the new dataset AiMDoom has more scenes, larger area size and different levels of difficulty. Intricate geometries and layouts, small doors and narrow corridors, the high diversity of scenes bring new challenges to the active mapping task. This benefits the whole community. 

2.	A novel approach for active mapping. The authors propose to predict the next best path (NBP) to find the next optimal location instead of directly predicting the one close to current position of the agent. The value map in NBP provides the best location and the obstacle map allows to use Dijkstra algorithm to find the shortest path from current location to the goal. This is a useful combination and brings inspiration to following works. 

3.	Impressive performance. The proposed approach obtains state-of-the-art performance on MP3D dataset and gives significantly better results than previous methods like MACARONS on the new dataset. Ablation studies show the effectiveness of the obstacle map.

4.	The paper is well-organized and easy to read.

### Weaknesses
I don’t see obvious weaknesses of this paper. Some of my concerns about the method and the dataset are as follows.

1. In L243, the point clouds are cropped at the current location of the agent. I am curious how does it work and what kind of parameters are used? My understanding is that the crop size may influence how much history information is used for the next path prediction.

2. In L245, the 3D point clouds are projected onto 2D image to simplify the processing. This strategy works for scenes with a single layer but may lose generalization ability in scenes with multiple layers as part of the depth information is discarded.

3. In the ablation study, the efficacy to the final reconstruction results of both the obstacle map and multi-task training are tested, however, it would be good to see the accuracy of the obstacle map itself and the value map itself instead of final reconstruction accuracy.

4. The new dataset is a synthetic dataset, so the domain gap may exist. As far as I know, a new version of Scannet dataset has been released. It has more scenes with more complicated geometry and structures. In the future, it might be possible to reorganize this new Scannet dataset and make a real complicated dataset.

### Questions
See the weaknesses section.

### Soundness
3

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
5

### Summary
This paper proposes a learning-based method to the problem of active 3D mapping of unknown environments. The method is hinged on next-best-path (NBP). It integrates a mapping progress encoder, a coverage gain decoder and an obstacle map decoder. The coverage gain and the obstacle map are used to compute the NBP. The NBP can direct the robot to reconstruct unseen environments with predicted long-term goals, achieving state-of-the-art performance on both the MP3D and AiMDoom datasets. The paper also contributes a dataset, AiMDoom, designed to benchmark active mapping in indoor scenes.

### Strengths
The idea of estimating NBP has good merit and shows promising results. The method is overall reasonably designed and the results are good. The evaluation demonstrates the strength of the proposed method.

### Weaknesses
The paper claims that the main novelty is the idea of next best path planning. It shows that NBP performs better than NBV which is reasonable and convincing. However, the method how NBP is computed is rather simplistic and the major technical components are actually the reconstructed map encoder and the two map decoders. With the estimated value map and obstacle map, NBP is computed in a straightforward way. On the other hand, training a network to predict value maps for scene coverage has good merit.

Some of the paths computed by the proposed method are too close to the walls, see Fig 4(b) left, making them collision-prone. The visualization of paths does not have to show shadows; showing the path on the ground could be clearer.

The experiment of spatial range of long-term goal is interesting. However, it would be more useful if more test can be conducted to find out how to choose the size of range for a given scene.

The proposed method is trained on the train split of AiMDoom. It is unclear whether the other alternative methods being compared were trained on AiMDoom or pretrained on other datasets. If so, the comparison would be unfair. More explanation is needed.

### Questions
No.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a path-planning algorithm for efficient 3D mapping. The core components of the NBP are the coverage gain decoder and obstacle map decoder, which are leveraged for long-term goal selection. The experiments showcase significant improvements against baselines. Besides, this paper also proposes a  new dataset called AiMDoom, which includes 400 scenes with different level of diffculty.

### Strengths
Developing methods for highly efficient exploration is an intriguing topic with potential applications across various navigation tasks. This paper provides comprehensive details on NPV techniques, and the dataset is expected to benefit the community by supporting further investigation into exploration strategies.

### Weaknesses
 - The scenes in AiMDoom contain minimal furniture or objects, resulting in mostly open space. This does not align with real-world environments, making these scenes suboptimal for training and evaluation purposes.

- The states described in papers L199 and L373 indicate that the proposed method operates within a 3-DoF domain. However, NBV tasks often involve planning in a 6-DoF camera pose space. Moreover, baseline methods, such as MACARONS and SCONE, support 6-DoF camera pose planning. A discussion is needed to explain why this paper considers only a 3-DoF setting.

- For 3-DoF trajectory planning, several well-known works exist, such as [1]. The authors should discuss why this paper’s approach offers advantages over previous works.



### Questions
- Do the obstacle map and value map encompass the entire scene? This could result in significant computational costs in large-scale environments.

- If the long-term goal is updated at each step, does this strategy enhance performance?

- In Table 2, `comp.` represents the average minimum distance between ground truth vertices and observations. However, the HM3D depth data should be noise-free. If I haven't overlooked any details, why is the `comp.` metric considered valid?

### Soundness
2

### Presentation
2

### Contribution
2
