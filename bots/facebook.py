# -*- coding: utf-8 -*-

"""
Copyright (c) 2018 hackbox developers (http://hackbox.io)
See the file 'LICENSE' for copying permission
"""

from time import sleep

from utils import log


def run(browser, account, is_first=True):
    log.status("Total points: {}".format(browser.execute_script("""
        return document.getElementsByClassName("points_count")[0].innerHTML;
    """)))
    sleep(5)
    if is_first:
        log.status("Opening facebook post like page...")
        browser.execute_script("""
            document.querySelector("a[href='/free_points/facebook_post_like']").click();
            """)

        log.ok("Done.")
        sleep(5)

    window_before = browser.window_handles[0]

    try:
        browser.execute_script("""
            document.querySelector(".single_like_button").click();
            """)
    except:
        browser.execute_script("""
        location.reload(); 
        """)
        run(browser, account, is_first)

    window_after = browser.window_handles[1]
    browser.switch_to_window(window_after)

    if is_first:
        try:
            browser.execute_script("""
                    var btns = document.getElementById("mobile_login_bar").getElementsByTagName("a");
                    if (btns[0].innerHTML == "Log In") {
                        btns[0].click();
                    } else {
                        btns[1].click();
                    }
                    """)
            sleep(2)
            browser.execute_script("""
                    document.getElementById("m_login_email").value = "{}";
                    document.getElementById("m_login_password").value = "{}";
                    document.querySelector("button[value='Log In']").click();
                    """.format(account["email"], account["password"]))
            sleep(3)
        except:
            browser.close()
            browser.switch_to_window(window_before)
            run(browser, account, is_first=True)

    try:
        browser.execute_script("""
            document.querySelector("a[data-sigil*='like-reaction-flyout']").click()
            """)
    except:
        pass
    sleep(5)

    browser.close()
    browser.switch_to_window(window_before)
    run(browser, account, is_first=False)
