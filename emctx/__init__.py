# Copyright 2021 DeepMind Technologies Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Mctx: Monte Carlo tree search in JAX."""

from emctx._src.action_selection import gumbel_muzero_interior_action_selection
from emctx._src.action_selection import gumbel_muzero_root_action_selection
from emctx._src.action_selection import GumbelMuZeroExtraData
from emctx._src.action_selection import muzero_action_selection
from emctx._src.base import ChanceRecurrentFnOutput
from emctx._src.base import DecisionRecurrentFnOutput
from emctx._src.base import InteriorActionSelectionFn
from emctx._src.base import LoopFn
from emctx._src.base import PolicyOutput
from emctx._src.base import RecurrentFn
from emctx._src.base import RecurrentFnOutput
from emctx._src.base import RecurrentState
from emctx._src.base import RootActionSelectionFn
from emctx._src.base import RootFnOutput
from emctx._src.policies import gumbel_muzero_policy
from emctx._src.policies import muzero_policy
from emctx._src.policies import stochastic_muzero_policy
from emctx._src.qtransforms import qtransform_by_min_max
from emctx._src.qtransforms import qtransform_by_parent_and_siblings
from emctx._src.qtransforms import qtransform_completed_by_mix_value
from emctx._src.search import search
from emctx._src.tree import Tree
# EMCTS additionals:
from emctx._src.action_selection import epistemic_muzero_action_selection
from emctx._src.action_selection import epistemic_gumbel_muzero_interior_action_selection
from emctx._src.action_selection import epistemic_gumbel_muzero_root_action_selection
from emctx._src.base import EpistemicRecurrentFnOutput
from emctx._src.base import EpistemicRootFnOutput
from emctx._src.base import EpistemicLoopFn
from emctx._src.base import EpistemicPolicyOutput
from emctx._src.base import EpistemicRecurrentFn
from emctx._src.policies import epistemic_muzero_policy
from emctx._src.policies import epistemic_gumbel_muzero_policy
from emctx._src.qtransforms import epistemic_qtransform_by_parent_and_siblings
from emctx._src.qtransforms import epistemic_qtransform_completed_by_mix_value
from emctx._src.epistemic_search import epistemic_search
from emctx._src.epistemic_tree import EpistemicTree

__version__ = "0.0.5"

__all__ = (
    "ChanceRecurrentFnOutput",
    "DecisionRecurrentFnOutput",
    "GumbelMuZeroExtraData",
    "InteriorActionSelectionFn",
    "LoopFn",
    "PolicyOutput",
    "RecurrentFn",
    "RecurrentFnOutput",
    "RecurrentState",
    "RootActionSelectionFn",
    "RootFnOutput",
    "Tree",
    "gumbel_muzero_interior_action_selection",
    "gumbel_muzero_policy",
    "gumbel_muzero_root_action_selection",
    "muzero_action_selection",
    "muzero_policy",
    "qtransform_by_min_max",
    "qtransform_by_parent_and_siblings",
    "qtransform_completed_by_mix_value",
    "search",
    "stochastic_muzero_policy",
    # EMCTS additionals:
    "EpistemicRecurrentFnOutput",
    "EpistemicRootFnOutput",
    "EpistemicLoopFn",
    "EpistemicPolicyOutput",
    "EpistemicRecurrentFn",
    "epistemic_muzero_policy",
    "epistemic_gumbel_muzero_policy",
    "epistemic_qtransform_by_parent_and_siblings",
    "epistemic_qtransform_completed_by_mix_value",
    "epistemic_muzero_action_selection",
    "epistemic_gumbel_muzero_interior_action_selection",
    "epistemic_gumbel_muzero_root_action_selection",
    "epistemic_search",
    "EpistemicTree",
)

#  _________________________________________
# / Please don't use symbols in `_src` they \
# \ are not part of the Mctx public API.    /
#  -----------------------------------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
#
