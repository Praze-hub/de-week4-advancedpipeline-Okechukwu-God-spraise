import textwrap
from pipeline.config import ConfigManager

def test_config_manager_reads_tmp_file(tmp_path):
    cfg = tmp_path / "pipeline.cfg"
    cfg.write_text(textwrap.dedent("""
                                    [api]
        base_url = https://example.com
        products_endpoint = /products
        users_endpoint = /users

        [pagination]
        limit = 7
                                   """))
    cm = ConfigManager(str(cfg))
    assert cm.get_base_url() == "https://example.com"
    assert cm.get_endpoint("products_endpoint") == "/products"
    assert cm.get_limit() == 7