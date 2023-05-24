import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { styled } from '@mui/material/styles';
import {
  AppBar,
  Toolbar,
  IconButton,
  Drawer,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Typography,
} from '@mui/material';
import { Menu as MenuIcon, Dashboard as DashboardIcon, Store as StoreIcon } from '@mui/icons-material';

const drawerWidth = 240;

const ContentContainer = styled('div')({
  flexGrow: 1,
  padding: '20px',
});

const Navbar: React.FC = () => {
  const [open, setOpen] = useState(false);

  const handleToggleDrawer = () => {
    setOpen(!open);
  };

  return (
    <div>
      <AppBar position="fixed">
        <Toolbar>
          <IconButton
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
            onClick={handleToggleDrawer}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Inventory Management
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer
        anchor="left"
        open={open}
        onClose={handleToggleDrawer}
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          '& .MuiDrawer-paper': {
            width: drawerWidth,
          },
        }}
      >
        <Toolbar />
        <List>
          <Link to="/MyComponent" style={{ textDecoration: 'none', color: 'inherit' }}>
            <ListItem button>
              <ListItemIcon>
                <DashboardIcon />
              </ListItemIcon>
              <ListItemText primary="Dashboard" />
            </ListItem>
          </Link>
          <Link to="/products" style={{ textDecoration: 'none', color: 'inherit' }}>
            <ListItem button>
              <ListItemIcon>
                <StoreIcon />
              </ListItemIcon>
              <ListItemText primary="Products" />
            </ListItem>
          </Link>
        </List>
      </Drawer>
      <ContentContainer>
      
      </ContentContainer>
    </div>
  );
};

export default Navbar;
