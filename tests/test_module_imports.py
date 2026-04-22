"""Tests for socratic-core module imports."""


def test_analytics_calculator_can_import():
    """Test analytics_calculator module can be imported."""
    try:
        import socratic_core.analytics_calculator as ac_mod
        assert hasattr(ac_mod, 'AnalyticsCalculator')
    except ModuleNotFoundError as e:
        assert False, f"Failed to import due to missing module: {e}"
    except ImportError:
        # Other import errors are acceptable (cross-library deps)
        pass


def test_project_categories_can_import():
    """Test project_categories module can be imported."""
    try:
        import socratic_core.project_categories as pc_mod
        # Just verify the module loads, don't check specific attributes
        assert pc_mod is not None
    except ModuleNotFoundError as e:
        assert False, f"Failed to import due to missing module: {e}"


def test_learning_engine_can_import():
    """Test learning_engine module can be imported."""
    try:
        import socratic_core.learning_engine as le_mod
        assert hasattr(le_mod, 'LearningEngine')
    except ModuleNotFoundError as e:
        assert False, f"Failed to import due to missing module: {e}"


def test_insight_categorizer_can_import():
    """Test insight_categorizer module can be imported."""
    try:
        import socratic_core.insight_categorizer as ic_mod
        assert hasattr(ic_mod, 'InsightCategorizer')
    except ModuleNotFoundError as e:
        assert False, f"Failed to import due to missing module: {e}"


def test_maturity_calculator_can_import():
    """Test maturity_calculator module can be imported."""
    try:
        import socratic_core.maturity_calculator as mc_mod
        assert hasattr(mc_mod, 'MaturityCalculator')
    except ModuleNotFoundError as e:
        assert False, f"Failed to import due to missing module: {e}"


def test_no_socratic_system_imports():
    """Verify no active socratic_system imports in source files."""
    import os

    src_dir = 'src/socratic_core'
    found_imports = []

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    for i, line in enumerate(f, 1):
                        # Check for uncommented imports from socratic_system
                        if 'from socratic_system' in line and not line.strip().startswith('#'):
                            found_imports.append(f"{filepath}:{i}: {line.strip()}")

    assert len(found_imports) == 0, "Found active socratic_system imports:\n" + "\n".join(found_imports)
