import { Navbar as FlowbiteNavbar, NavbarBrand, NavbarCollapse, NavbarLink, NavbarToggle } from "flowbite-react";
export function Navbar() {
    return (
        <FlowbiteNavbar fluid rounded>
            <NavbarBrand href="https://flowbite-react.com">
                <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite React</span>
            </NavbarBrand>
            <NavbarToggle />
            <NavbarCollapse>
                <NavbarLink href="#" active>
                    Home
                </NavbarLink>
            </NavbarCollapse>
        </FlowbiteNavbar>
    );
}
