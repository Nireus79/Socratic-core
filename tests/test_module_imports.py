"""Tests for socratic-core module imports."""

import sys


def test_analytics_calculator_can_import():
    """Test analytics_calculator module can be imported."""
    # Just import the module, don't try to instantiate
    try:
        import socratic_core.analytics_calculator as ac_mod
        assert hasattr(ac_mod, 'AnalyticsCalculator')
    except ImportError as e:
        assert False, f"Failed to import analytics_calculator: {e}"


def test_project_categories_can_import():
    """Test project_categories module can be imported."""
    try:
        import socratic_core.project_categories as pc_mod
        assert hasattr(pc_mod, 'get_phase_categories')
        assert hasattr(pc_mod, 'PROJECT_TYPES')
    except ImportError as e:
        assert False, f"Failed to import project_categories: {e}"


def test_learning_engine_can_import():
    """Test learning_engine module can be imported."""
    try:
        import socratic_core.learning_engine as le_mod
        assert hasattr(le_mod, 'LearningEngine')
    except ImportError as e:
        assert False, f"Failed to import learning_engine: {e}"


def test_insight_categorizer_can_import():
    """Test insight_categorizer module can be imported."""
    try:
        import socratic_core.insight_categorizer as ic_mod
        assert hasattr(ic_mod, 'InsightCategorizer')
    except ImportError as e:
        assert False, f"Failed to import insight_categorizer: {e}"
